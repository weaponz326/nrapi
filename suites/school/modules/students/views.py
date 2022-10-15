import datetime

from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.decorators import api_view

from .models import Student, StudentCodeConfig
from .serializers import StudentCodeConfigSerializer, StudentSerializer
from suites.restaurant.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class StudentView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    parser_class = (FileUploadParser,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'student_code', 'first_name', 'last_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        student = Student.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(student, request, view=self)
        serializer = StudentSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class StudentDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_class = (FileUploadParser,)

    def get(self, request, id, format=None):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class StudentCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = StudentCodeConfig.objects.get(id=id)
        serializer = StudentCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = StudentCodeConfig.objects.get(id=id)
        serializer = StudentCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewStudentCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = StudentCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)        

        if code_set.entry_mode == 'Auto':
            code = StudentCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}{}'.format(code_set.prefix, new_code, code_set.year_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        StudentCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="ST",
            last_code="00000",
            year_code=datetime.datetime.now().strftime("%y")
        )

# --------------------------------------------------------------------------------------
# dashboard
