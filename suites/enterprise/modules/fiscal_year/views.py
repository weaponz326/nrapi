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

from .models import ActiveFiscalYear, FiscalYear, FiscalYearCodeConfig
from .serializers import ActiveFiscalYearSerializer, FiscalYearCodeConfigSerializer, FiscalYearSerializer
from suites.enterprise.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class FiscalYearView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'year_code', 'year_name', 'year_status')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        year = FiscalYear.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(year, request, view=self)
        serializer = FiscalYearSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = FiscalYearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class FiscalYearDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        year = FiscalYear.objects.get(id=id)
        serializer = FiscalYearSerializer(year)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        year = FiscalYear.objects.get(id=id)
        serializer = FiscalYearSerializer(year, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        year = FiscalYear.objects.get(id=id)
        year.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# active year

class ActiveFiscalYearDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        active_year = ActiveFiscalYear.objects.get(id=id)
        serializer = ActiveFiscalYearSerializer(active_year)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        active_year = ActiveFiscalYear.objects.get(id=id)
        serializer = ActiveFiscalYearSerializer(active_year, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        ActiveFiscalYear.objects.create(
            id=instance.id,
        )

# --------------------------------------------------------------------------------------
# config

class FiscalYearCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = FiscalYearCodeConfig.objects.get(id=id)
        serializer = FiscalYearCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = FiscalYearCodeConfig.objects.get(id=id)
        serializer = FiscalYearCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewFiscalYearCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = FiscalYearCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = FiscalYearCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        FiscalYearCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="TM",
            last_code="000"
        )

# --------------------------------------------------------------------------------------
# dashboard

