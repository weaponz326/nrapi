import datetime
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from suites.personal.users.models import User
from .models import Account, AccountCodeConfig, Transaction
from .serializers import AccountCodeConfigSerializer, AccountSerializer, TransactionSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class AccountView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'account_name', 'account_number', 'bank_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        account = Account.objects.filter(user=user).order_by('-created_at')
        results = self.paginate_queryset(account, request, view=self)
        serializer = AccountSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AccountDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        account = Account.objects.get(id=id)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        account = Account.objects.get(id=id)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        account = Account.objects.get(id=id)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------------------------------
# transactions

class TransactionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        transaction = Transaction.objects.filter(account=account).order_by('-created_at')
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TransactionDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        transaction = Transaction.objects.get(id=id)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        transaction = Transaction.objects.get(id=id)
        serializer = TransactionSerializer(transaction, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        transaction = Transaction.objects.get(id=id)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# all transactions
class AllTransactionsView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'transaction_date', 'account__account_name', 'account__bank_name', 'description', 'transaction_type', 'amount']
    ordering = ['-created_at']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        account = Transaction.objects.filter(account__user=user)
        results = self.paginate_queryset(account, request, view=self)
        serializer = TransactionSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

# --------------------------------------------------------------------------------------
# config

class AccountCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = AccountCodeConfig.objects.get(id=id)
        serializer = AccountCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = AccountCodeConfig.objects.get(id=id)
        serializer = AccountCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewAccountCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = AccountCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = AccountCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=User)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        AccountCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.first_name) + get_initials(instance.last_name),
            suffix="AC",
            last_code="000"
        )
        
# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def all_account_count(request):
    count = Account.objects\
        .filter(user__id=request.query_params.get('user', None))\
        .count()            
    content = {'count': count}
    return Response(content)

@api_view()
def transaction_share(request):
    credit = Transaction.objects\
        .filter(account__user__id=request.query_params.get('user', None), transaction_type = "Credit")\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .aggregate(Sum('amount'))
    
    debit = Transaction.objects\
        .filter(account__user__id=request.query_params.get('user', None), transaction_type = "Debit")\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .aggregate(Sum('amount'))
                    
    content = {'credit': credit['amount__sum'], 'debit': debit['amount__sum']}
    return Response(content)

@api_view()
def transaction_annotate(request):
    credit_items = Transaction.objects\
        .filter(account__user__id=request.query_params.get('user', None), transaction_type = "Credit")\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Sum('amount')).order_by('-date')
    filled_credit_items = fiil_zero_dates(credit_items)

    debit_items = Transaction.objects\
        .filter(account__user__id=request.query_params.get('user', None), transaction_type = "Debit")\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Sum('amount')).order_by('-date')
    filled_debit_items = fiil_zero_dates(debit_items)

    content = {'credit': filled_credit_items, 'debit': filled_debit_items}
    return Response(content)
