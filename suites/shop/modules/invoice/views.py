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

from .models import Invoice, InvoiceCodeConfig, InvoiceItem
from .serializers import InvoiceCodeConfigSerializer, InvoiceSerializer, InvoiceItemSerializer
from suites.shop.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class InvoiceView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'invoice_code', 'invoice_date', 'customer_name', 'invoice_status', 'total_amount']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        invoice = Invoice.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(invoice, request, view=self)
        serializer = InvoiceSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = InvoiceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class InvoiceDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        invoice = Invoice.objects.get(id=id)
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        invoice = Invoice.objects.get(id=id)
        serializer = InvoiceSerializer(invoice, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        invoice = Invoice.objects.get(id=id)
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# invoice item

class InvoiceItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        invoice = self.request.query_params.get('invoice', None)
        item = InvoiceItem.objects.filter(invoice=invoice).order_by('created_at')
        serializer = InvoiceItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # TODO:
        # insert into deliveries if invoice_type == delivery

        serializer = InvoiceItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class InvoiceItemDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        item = InvoiceItem.objects.get(id=id)
        serializer = InvoiceItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = InvoiceItem.objects.get(id=id)
        serializer = InvoiceItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = InvoiceItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class InvoiceCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = InvoiceCodeConfig.objects.get(id=id)
        serializer = InvoiceCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = InvoiceCodeConfig.objects.get(id=id)
        serializer = InvoiceCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewInvoiceCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = InvoiceCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = InvoiceCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        InvoiceCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="IN",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def invoice_count(request):
    count = Invoice.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def invoice_annotate(request):
    items = Invoice.objects\
        .filter(account=request.query_params.get('account', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_items = fiil_zero_dates(items)
    return Response(filled_items)
