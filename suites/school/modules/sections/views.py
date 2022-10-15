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

from .models import Section, SectionCodeConfig, SectionStudent
from .serializers import SectionCodeConfigSerializer, SectionSerializer, SectionStudentSerializer
from suites.restaurant.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class SectionView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'section_code', 'section_name')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        section = Section.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(section, request, view=self)
        serializer = SectionSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SectionDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        section = Section.objects.get(id=id)
        serializer = SectionSerializer(section)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        section = Section.objects.get(id=id)
        serializer = SectionSerializer(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        section = Section.objects.get(id=id)
        section.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# section students

class SectionStudentView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'section', 'student')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        section = self.request.query_params.get('section', None)
        section_student = SectionStudent.objects.filter(section=section).order_by('-created_at')
        results = self.paginate_queryset(section_student, request, view=self)
        serializer = SectionStudentSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SectionStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SectionStudentDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        section_student = SectionStudent.objects.get(id=id)
        serializer = SectionStudentSerializer(section_student)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        section_student = SectionStudent.objects.get(id=id)
        serializer = SectionStudentSerializer(section_student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        section_student = SectionStudent.objects.get(id=id)
        section_student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class SectionCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = SectionCodeConfig.objects.get(id=id)
        serializer = SectionCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = SectionCodeConfig.objects.get(id=id)
        serializer = SectionCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewSectionCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = SectionCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = SectionCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        SectionCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="SU",
            last_code="0000"
        )

# --------------------------------------------------------------------------------------
# dashboard

