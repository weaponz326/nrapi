import datetime

from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
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

from .models import Diagnosis, DiagnosisCodeConfig, DiagnosisReport
from .serializers import DiagnosisCodeConfigSerializer, DiagnosisReportSerializer, DiagnosisSerializer
from suites.hospital.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class DiagnosisView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'diagnosis_code', 'diagnosis_date', 'consultant_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        diagnosis = Diagnosis.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(diagnosis, request, view=self)
        serializer = DiagnosisSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DiagnosisSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DiagnosisDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        diagnosis = Diagnosis.objects.get(id=id)
        serializer = DiagnosisSerializer(diagnosis)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        diagnosis = Diagnosis.objects.get(id=id)
        serializer = DiagnosisSerializer(diagnosis, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        diagnosis = Diagnosis.objects.get(id=id)
        diagnosis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# diagnosis report

class DiagnosisReportDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        diagnosis = DiagnosisReport.objects.get(id=id)
        serializer = DiagnosisReportSerializer(diagnosis)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        diagnosis = DiagnosisReport.objects.get(id=id)
        serializer = DiagnosisReportSerializer(diagnosis, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        diagnosis = DiagnosisReport.objects.get(id=id)
        diagnosis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Diagnosis)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        DiagnosisReport.objects.create(
            id=instance.id,
        )

# --------------------------------------------------------------------------------------
# config

class DiagnosisCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = DiagnosisCodeConfig.objects.get(id=id)
        serializer = DiagnosisCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = DiagnosisCodeConfig.objects.get(id=id)
        serializer = DiagnosisCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewDiagnosisCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = DiagnosisCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = DiagnosisCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        DiagnosisCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="DS",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def diagnosis_count(request):
    count = Diagnosis.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)
