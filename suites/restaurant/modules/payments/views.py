import datetime
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.db.models import Sum

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import Payment
from .serializers import PaymentSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fillZeroDates


# Create your views here.

class PaymentView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'payment_code', 'amount_paid', 'order.order_code', 'order.customer_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        payment = Payment.objects.filter(account=account)
        results = self.paginate_queryset(payment, request, view=self)
        serializer = PaymentSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PaymentDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        payment = Payment.objects.get(id=id)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        payment = Payment.objects.get(id=id)
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        payment = Payment.objects.get(id=id)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def payment_count(request):
    count = Payment.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def payment_total(request):
    amount = Payment.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .aggregate(Sum('amount_paid'))                 
    content = {'total': amount['amount_paid__sum']}
    return Response(content)

@api_view()
def payment_annotate(request):
    items = Payment.objects\
        .filter(account=request.query_params.get('account', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Sum('amount_paid')).order_by('-date')
    filled_items = fillZeroDates(items)
    return Response(filled_items)