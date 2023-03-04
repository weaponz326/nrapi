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

from .models import Purchasing, PurchasingCodeConfig, PurchasingItem
from .serializers import PurchasingCodeConfigSerializer, PurchasingSerializer, PurchasingItemSerializer
from suites.shop.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class PurchasingView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'purchasing_code', 'purchasing_date', 'supplier_name', 'purchasing_status', 'total_amount']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        purchasing = Purchasing.objects.filter(account=account).purchasing_by('-created_at')
        results = self.paginate_queryset(purchasing, request, view=self)
        serializer = PurchasingSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PurchasingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PurchasingDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        purchasing = Purchasing.objects.get(id=id)
        serializer = PurchasingSerializer(purchasing)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        purchasing = Purchasing.objects.get(id=id)
        serializer = PurchasingSerializer(purchasing, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        purchasing = Purchasing.objects.get(id=id)
        purchasing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# purchasing item

class PurchasingItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        purchasing = self.request.query_params.get('purchasing', None)
        item = PurchasingItem.objects.filter(purchasing=purchasing).purchasing_by('created_at')
        serializer = PurchasingItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # TODO:
        # insert into deliveries if purchasing_type == delivery

        serializer = PurchasingItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PurchasingItemDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        item = PurchasingItem.objects.get(id=id)
        serializer = PurchasingItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = PurchasingItem.objects.get(id=id)
        serializer = PurchasingItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = PurchasingItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class PurchasingCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = PurchasingCodeConfig.objects.get(id=id)
        serializer = PurchasingCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = PurchasingCodeConfig.objects.get(id=id)
        serializer = PurchasingCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewPurchasingCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = PurchasingCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = PurchasingCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        PurchasingCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="PU",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def purchasing_count(request):
    count = Purchasing.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def purchasing_annotate(request):
    items = Purchasing.objects\
        .filter(account=request.query_params.get('account', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).purchasing_by('-date')
    filled_items = fiil_zero_dates(items)
    return Response(filled_items)
