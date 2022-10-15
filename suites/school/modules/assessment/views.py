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

from .models import Assessment, AssessmentCodeConfig, AssessmentClass
from .serializers import AssessmentCodeConfigSerializer, AssessmentSerializer, AssessmentClassSerializer
from suites.restaurant.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class AssessmentView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'assessment_code', 'assessment_name', 'assessment_date', 'subject')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        assessment = Assessment.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(assessment, request, view=self)
        serializer = AssessmentSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AssessmentDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        assessment = Assessment.objects.get(id=id)
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        assessment = Assessment.objects.get(id=id)
        serializer = AssessmentSerializer(assessment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        assessment = Assessment.objects.get(id=id)
        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# assessment classs

class AssessmentClassView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'assessment', 'class')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        assessment = self.request.query_params.get('assessment', None)
        assessment_class = AssessmentClass.objects.filter(assessment=assessment).order_by('-created_at')
        results = self.paginate_queryset(assessment_class, request, view=self)
        serializer = AssessmentClassSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AssessmentClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AssessmentClassDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        assessment_class = AssessmentClass.objects.get(id=id)
        serializer = AssessmentClassSerializer(assessment_class)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        assessment_class = AssessmentClass.objects.get(id=id)
        serializer = AssessmentClassSerializer(assessment_class, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        assessment_class = AssessmentClass.objects.get(id=id)
        assessment_class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# sheet

# TODO:

# --------------------------------------------------------------------------------------
# config

class AssessmentCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = AssessmentCodeConfig.objects.get(id=id)
        serializer = AssessmentCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = AssessmentCodeConfig.objects.get(id=id)
        serializer = AssessmentCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewAssessmentCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = AssessmentCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = AssessmentCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        AssessmentCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="AS",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

