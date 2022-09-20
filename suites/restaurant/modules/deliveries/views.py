import datetime
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import Delivery
from .serializers import DeliverySerializer
from suites.restaurant.modules.orders.models import Order
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fillZeroDates


# Create your views here.

class DeliveryView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'delivery_date', 'delivery_location', 'delivery_status', 'order.order_code', 'order.order_date']
    ordering = ['-created_at']
    
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        delivery = Delivery.objects.filter(account=account)
        results = self.paginate_queryset(delivery, request, view=self)
        serializer = DeliverySerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        if Delivery.objects.filter(id=request.data.get('id')).exists():
            return Response("exists")
        else:
            serializer = DeliverySerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(id=request.data.get('id'))
                return Response(serializer.data)
            return Response(serializer.errors)

class DeliveryDetailView(APIView):
    def get(self, request, id, format=None):
        if Delivery.objects.filter(id=id).exists():
            delivery = Delivery.objects.get(id=id)
            serializer = DeliverySerializer(delivery)
            return Response(serializer.data)
        else:
            return Response('not exist')

    def put(self, request, id, format=None):
        delivery = Delivery.objects.get(id=id)
        serializer = DeliverySerializer(delivery, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        delivery = Delivery.objects.get(id=id)
        delivery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def delivery_count(request):
    count = Delivery.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def delivery_annotate(request):
    items = Delivery.objects\
        .filter(account=request.query_params.get('account', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_items = fillZeroDates(items)
    return Response(filled_items)
