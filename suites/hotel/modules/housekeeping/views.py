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

from .models import Housekeeping, HousekeepingCodeConfig, Checklist
from .serializers import HousekeepingCodeConfigSerializer, HousekeepingSerializer, ChecklistSerializer
from suites.hotel.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class HousekeepingView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'housekeeping_code', 'housekeeping_date', 'customer_name', 'housekeeping_type', 'total_amount']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        housekeeping = Housekeeping.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(housekeeping, request, view=self)
        serializer = HousekeepingSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = HousekeepingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class HousekeepingDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        housekeeping = Housekeeping.objects.get(id=id)
        serializer = HousekeepingSerializer(housekeeping)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        housekeeping = Housekeeping.objects.get(id=id)
        serializer = HousekeepingSerializer(housekeeping, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        housekeeping = Housekeeping.objects.get(id=id)
        housekeeping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# housekeeping item

class ChecklistView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        housekeeping = self.request.query_params.get('housekeeping', None)
        item = Checklist.objects.filter(housekeeping=housekeeping).order_by('created_at')
        serializer = ChecklistSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # TODO:
        # insert into deliveries if housekeeping_type == delivery

        serializer = ChecklistSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ChecklistDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        item = Checklist.objects.get(id=id)
        serializer = ChecklistSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = Checklist.objects.get(id=id)
        serializer = ChecklistSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = Checklist.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class HousekeepingCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = HousekeepingCodeConfig.objects.get(id=id)
        serializer = HousekeepingCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = HousekeepingCodeConfig.objects.get(id=id)
        serializer = HousekeepingCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewHousekeepingCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = HousekeepingCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = HousekeepingCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        HousekeepingCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="HK",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def housekeeping_count(request):
    count = Housekeeping.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def housekeeping_annotate(request):
    items = Housekeeping.objects\
        .filter(account=request.query_params.get('account', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_items = fiil_zero_dates(items)
    return Response(filled_items)
