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

from .models import Subject, SubjectCodeConfig, SubjectTeacher
from .serializers import SubjectCodeConfigSerializer, SubjectSerializer, SubjectTeacherSerializer
from suites.school.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class SubjectView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'subject_code', 'subject_name', 'department')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        subject = Subject.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(subject, request, view=self)
        serializer = SubjectSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SubjectDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        subject = Subject.objects.get(id=id)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        subject = Subject.objects.get(id=id)
        serializer = SubjectSerializer(subject, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        subject = Subject.objects.get(id=id)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# subject teachers

class SubjectTeacherView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'subject', 'teacher')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        subject = self.request.query_params.get('subject', None)
        subject_teacher = SubjectTeacher.objects.filter(subject=subject).order_by('-created_at')
        serializer = SubjectTeacherSerializer(subject_teacher, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubjectTeacherSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SubjectTeacherDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        subject_teacher = SubjectTeacher.objects.get(id=id)
        serializer = SubjectTeacherSerializer(subject_teacher)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        subject_teacher = SubjectTeacher.objects.get(id=id)
        serializer = SubjectTeacherSerializer(subject_teacher, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        subject_teacher = SubjectTeacher.objects.get(id=id)
        subject_teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class SubjectCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = SubjectCodeConfig.objects.get(id=id)
        serializer = SubjectCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = SubjectCodeConfig.objects.get(id=id)
        serializer = SubjectCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewSubjectCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = SubjectCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = SubjectCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        SubjectCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="SU",
            last_code="0000"
        )

# --------------------------------------------------------------------------------------
# dashboard

