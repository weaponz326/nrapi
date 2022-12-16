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

from .models import Report, ReportCodeConfig, ReportAssessment
from .serializers import ReportCodeConfigSerializer, ReportSerializer, ReportAssessmentSerializer
from suites.school.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class ReportView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'report_code', 'report_name', 'report_date', 'clase')
    ordering = ('-created_at')

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        report = Report.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(report, request, view=self)
        serializer = ReportSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ReportSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ReportDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        report = Report.objects.get(id=id)
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        report = Report.objects.get(id=id)
        serializer = ReportSerializer(report, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        report = Report.objects.get(id=id)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# report assessments

class ReportAssessmentView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'report', 'assessment')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        report = self.request.query_params.get('report', None)
        report_assessment = ReportAssessment.objects.filter(report=report).order_by('-created_at')
        results = self.paginate_queryset(report_assessment, request, view=self)
        serializer = ReportAssessmentSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ReportAssessmentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ReportAssessmentDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        report_assessment = ReportAssessment.objects.get(id=id)
        serializer = ReportAssessmentSerializer(report_assessment)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        report_assessment = ReportAssessment.objects.get(id=id)
        serializer = ReportAssessmentSerializer(report_assessment, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        report_assessment = ReportAssessment.objects.get(id=id)
        report_assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# report sheet

# TODO:

# --------------------------------------------------------------------------------------
# config

class ReportCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = ReportCodeConfig.objects.get(id=id)
        serializer = ReportCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = ReportCodeConfig.objects.get(id=id)
        serializer = ReportCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewReportCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = ReportCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = ReportCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        ReportCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="RP",
            last_code="0000"
        )

# --------------------------------------------------------------------------------------
# dashboard
