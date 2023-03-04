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

from .models import Payable, PayableCodeConfig
from .serializers import PayableCodeConfigSerializer, PayableSerializer
from suites.shop.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class PayableView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'payable_code', 'payable_date', 'due_date', 'amount', 'customer_name', 'date_paid']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        payable = Payable.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(payable, request, view=self)
        serializer = PayableSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PayableSerializer(data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PayableDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        payable = Payable.objects.get(id=id)
        serializer = PayableSerializer(payable)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        payable = Payable.objects.get(id=id)
        serializer = PayableSerializer(payable, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        payable = Payable.objects.get(id=id)
        payable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class PayableCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = PayableCodeConfig.objects.get(id=id)
        serializer = PayableCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = PayableCodeConfig.objects.get(id=id)
        serializer = PayableCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewPayableCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = PayableCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = PayableCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        PayableCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="RE",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def payable_count(request):
    count = Payable.objects\
        .filter(account=request.query_params.get('account', None))\
        .count()            
    content = {'count': count}
    return Response(content)
