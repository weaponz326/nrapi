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

from .models import AttendanceCodeConfig, StudentAttendance, TeacherAttendance
from .serializers import AttendanceCodeConfigSerializer, StudentAttendanceSerializer, TeacherAttendanceSerializer
from suites.school.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

# student attendance

class StudentAttendanceView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'attendance_code', 'attendance_name', 'attendance_date', 'class')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        attendance = StudentAttendance.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(attendance, request, view=self)
        serializer = StudentAttendanceSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentAttendanceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class StudentAttendanceDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        attendance = StudentAttendance.objects.get(id=id)
        serializer = StudentAttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        attendance = StudentAttendance.objects.get(id=id)
        serializer = StudentAttendanceSerializer(attendance, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        attendance = StudentAttendance.objects.get(id=id)
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# teacher attendance

class TeacherAttendanceView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'attendance_code', 'attendance_name', 'attendance_date')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        attendance = TeacherAttendance.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(attendance, request, view=self)
        serializer = TeacherAttendanceSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TeacherAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TeacherAttendanceDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        attendance = TeacherAttendance.objects.get(id=id)
        serializer = TeacherAttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        attendance = TeacherAttendance.objects.get(id=id)
        serializer = TeacherAttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        attendance = TeacherAttendance.objects.get(id=id)
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# student sheet

# TODO:

# --------------------------------------------------------------------------------------
# teacher sheet

# TODO:

# --------------------------------------------------------------------------------------
# config

class AttendanceCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = AttendanceCodeConfig.objects.get(id=id)
        serializer = AttendanceCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = AttendanceCodeConfig.objects.get(id=id)
        serializer = AttendanceCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewAttendanceCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = AttendanceCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = AttendanceCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        AttendanceCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="AT",
            last_code="0000"
        )

# --------------------------------------------------------------------------------------
# dashboard

