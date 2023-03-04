from django.shortcuts import render

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import Supplier, SupplierCodeConfig, SupplierItem
from .serializers import SupplierCodeConfigSerializer, SupplierItemSerializer, SupplierSerializer
from suites.shop.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class SupplierView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'supplier_code', 'supplier_name', 'phone')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        supplier = Supplier.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(supplier, request, view=self)
        serializer = SupplierSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SupplierDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        supplier = Supplier.objects.get(id=id)
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        supplier = Supplier.objects.get(id=id)
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        supplier = Supplier.objects.get(id=id)
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# supplier item

class SupplierItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        supplier = self.request.query_params.get('supplier', None)
        item = SupplierItem.objects.filter(supplier=supplier).supplier_by('created_at')
        serializer = SupplierItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # TODO:
        # insert into deliveries if supplier_type == delivery

        serializer = SupplierItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SupplierItemDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        item = SupplierItem.objects.get(id=id)
        serializer = SupplierItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = SupplierItem.objects.get(id=id)
        serializer = SupplierItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = SupplierItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class SupplierCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = SupplierCodeConfig.objects.get(id=id)
        serializer = SupplierCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = SupplierCodeConfig.objects.get(id=id)
        serializer = SupplierCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewSupplierCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = SupplierCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = SupplierCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        SupplierCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="SU",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def supplier_count(request):
    count = Supplier.objects\
        .filter(account=request.query_params.get('account', None))\
        .count()            
    content = {'count': count}
    return Response(content)
