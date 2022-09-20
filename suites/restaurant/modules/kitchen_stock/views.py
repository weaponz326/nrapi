from django.shortcuts import render
from django.db.models import Count

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import StockItem
from .serializers import StockItemSerializer
from accounts.paginations import TablePagination


# Create your views here.

class StockItemView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'item_code', 'item_name', 'quantity', 'category', 'item_type', 'refill_ordered']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        item = StockItem.objects.filter(account=account)
        results = self.paginate_queryset(item, request, view=self)
        serializer = StockItemSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = StockItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class StockItemDetailView(APIView):
    def get(self, request, id, format=None):
        item = StockItem.objects.get(id=id)
        serializer = StockItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = StockItem.objects.get(id=id)
        serializer = StockItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = StockItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def stock_item_count(request):
    count = StockItem.objects\
        .filter(account=request.query_params.get('account', None))\
        .count()            
    content = {'count': count}
    return Response(content)

@api_view()
def out_of_stock_count(request):
    count = StockItem.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(quantity=0)\
        .count()            
    content = {'count': count}
    return Response(content)