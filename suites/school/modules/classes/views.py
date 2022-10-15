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

from .models import Clase, ClassStudent, Department
from .serializers import ClassSerializer, ClassStudentSerializer, DepartmentSerializer
from suites.restaurant.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class ClassView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'class_name', 'grade', 'department')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        clase = Clase.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(clase, request, view=self)
        serializer = ClassSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ClassDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        clase = Clase.objects.get(id=id)
        serializer = ClassSerializer(clase)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        clase = Clase.objects.get(id=id)
        serializer = ClassSerializer(clase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        clase = Clase.objects.get(id=id)
        clase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# class students

class ClassStudentView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'clase', 'student')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        clase = self.request.query_params.get('clase', None)
        class_student = ClassStudent.objects.filter(clase=clase).order_by('-created_at')
        results = self.paginate_queryset(class_student, request, view=self)
        serializer = ClassStudentSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ClassStudentDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        class_student = ClassStudent.objects.get(id=id)
        serializer = ClassStudentSerializer(class_student)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        class_student = ClassStudent.objects.get(id=id)
        serializer = ClassStudentSerializer(class_student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        class_student = ClassStudent.objects.get(id=id)
        class_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# department

class DepartmentView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'department_name', 'department_head')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        department = Department.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(department, request, view=self)
        serializer = DepartmentSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DepartmentDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        department = Department.objects.get(id=id)
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        department = Department.objects.get(id=id)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        department = Department.objects.get(id=id)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# dashboard

