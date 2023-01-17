import datetime

from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import Bill, CheckinCharge, BillCodeConfig, ServiceCharge
from .serializers import CheckinChargeSerializer, BillCodeConfigSerializer, BillSerializer, ServiceChargeSerializer
from suites.hotel.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class BillView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'bill_code', 'bill_date', 'guest_name', 'total_amount']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        bill = Bill.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(bill, request, view=self)
        serializer = BillSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BillSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BillDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        bill = Bill.objects.get(id=id)
        serializer = BillSerializer(bill)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        bill = Bill.objects.get(id=id)
        serializer = BillSerializer(bill, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        bill = Bill.objects.get(id=id)
        bill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# checkin charges

class CheckinChargeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        bill = self.request.query_params.get('bill', None)
        charge = CheckinCharge.objects.filter(bill=bill).order_by('created_at')
        serializer = CheckinChargeSerializer(charge, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CheckinChargeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CheckinChargeDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        charge = CheckinCharge.objects.get(id=id)
        serializer = CheckinChargeSerializer(charge)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        charge = CheckinCharge.objects.get(id=id)
        serializer = CheckinChargeSerializer(charge, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        charge = CheckinCharge.objects.get(id=id)
        charge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# service charges

class ServiceChargeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        bill = self.request.query_params.get('bill', None)
        charge = ServiceCharge.objects.filter(bill=bill).order_by('created_at')
        serializer = ServiceChargeSerializer(charge, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServiceChargeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ServiceChargeDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        charge = ServiceCharge.objects.get(id=id)
        serializer = ServiceChargeSerializer(charge)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        charge = ServiceCharge.objects.get(id=id)
        serializer = ServiceChargeSerializer(charge, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        charge = ServiceCharge.objects.get(id=id)
        charge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class BillCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = BillCodeConfig.objects.get(id=id)
        serializer = BillCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = BillCodeConfig.objects.get(id=id)
        serializer = BillCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewBillCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = BillCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = BillCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        BillCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="BL",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def bill_count(request):
    count = Bill.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def bill_annotate(request):
    items = Bill.objects\
        .filter(account=request.query_params.get('account', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_items = fiil_zero_dates(items)
    return Response(filled_items)
