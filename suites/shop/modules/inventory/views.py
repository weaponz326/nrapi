from django.shortcuts import render
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import Inventory, InventoryCodeConfig
from .serializers import InventoryCodeConfigSerializer, InventorySerializer
from suites.shop.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class InventoryView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'inventory_code', 'product_name', 'stock', 'location', 'batch_number']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        inventory = Inventory.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(inventory, request, view=self)
        serializer = InventorySerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = InventorySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class InventoryDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        inventory = Inventory.objects.get(id=id)
        serializer = InventorySerializer(inventory)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        inventory = Inventory.objects.get(id=id)
        serializer = InventorySerializer(inventory, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        inventory = Inventory.objects.get(id=id)
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class InventoryCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = InventoryCodeConfig.objects.get(id=id)
        serializer = InventoryCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = InventoryCodeConfig.objects.get(id=id)
        serializer = InventoryCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewInventoryCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = InventoryCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = InventoryCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        InventoryCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="IY",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def inventory_count(request):
    count = Inventory.objects\
        .filter(account=request.query_params.get('account', None))\
        .count()            
    content = {'count': count}
    return Response(content)

@api_view()
def out_of_stock_count(request):
    count = Inventory.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(quantity=0)\
        .count()            
    content = {'count': count}
    return Response(content)