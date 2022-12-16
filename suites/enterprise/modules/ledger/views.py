import datetime
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.db.models import Sum

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import Ledger, LedgerItem
from .serializers import LedgerSerializer, LedgerItemSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates


# Create your views here.

class LedgerView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'ledger_code', 'ledger_name', 'reference_number']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        ledger = Ledger.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(ledger, request, view=self)
        serializer = LedgerSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = LedgerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class LedgerDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        ledger = Ledger.objects.get(id=id)
        serializer = LedgerSerializer(ledger)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        ledger = Ledger.objects.get(id=id)
        serializer = LedgerSerializer(ledger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        ledger = Ledger.objects.get(id=id)
        ledger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------------------------------
# ledger items

class LedgerItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        ledger = self.request.query_params.get('ledger', None)
        item = LedgerItem.objects.filter(ledger=ledger).order_by('-created_at')
        serializer = LedgerItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LedgerItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class LedgerItemDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        item = LedgerItem.objects.get(id=id)
        serializer = LedgerItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = LedgerItem.objects.get(id=id)
        serializer = LedgerItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = LedgerItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# all items
class AllLedgerItemsView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'item_date', 'ledger__ledger_name', 'ledger__bank_name', 'description', 'item_type', 'amount']
    ordering = ['-created_at']

    def get(self, request, format=None):
        ledger = self.request.query_params.get('ledger', None)
        ledger = LedgerItem.objects.filter(ledger__ledger=ledger)
        results = self.paginate_queryset(ledger, request, view=self)
        serializer = LedgerItemSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def all_ledger_count(request):
    count = Ledger.objects\
        .filter(user__id=request.query_params.get('user', None))\
        .count()            
    content = {'count': count}
    return Response(content)

@api_view()
def item_share(request):
    credit = LedgerItem.objects\
        .filter(ledger__user__id=request.query_params.get('user', None), item_type = "Credit")\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .aggregate(Sum('amount'))
    
    debit = LedgerItem.objects\
        .filter(ledger__user__id=request.query_params.get('user', None), item_type = "Debit")\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .aggregate(Sum('amount'))
                    
    content = {'credit': credit['amount__sum'], 'debit': debit['amount__sum']}
    return Response(content)

@api_view()
def item_annotate(request):
    credit_items = LedgerItem.objects\
        .filter(ledger__user__id=request.query_params.get('user', None), item_type = "Credit")\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Sum('amount')).order_by('-date')
    filled_credit_items = fiil_zero_dates(credit_items)

    debit_items = LedgerItem.objects\
        .filter(ledger__user__id=request.query_params.get('user', None), item_type = "Debit")\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Sum('amount')).order_by('-date')
    filled_debit_items = fiil_zero_dates(debit_items)

    content = {'credit': filled_credit_items, 'debit': filled_debit_items}
    return Response(content)
