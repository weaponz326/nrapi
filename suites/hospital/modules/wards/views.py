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

from .models import Ward, WardCodeConfig, WardPatient
from .serializers import WardCodeConfigSerializer, WardSerializer, WardPatientSerializer
from suites.hospital.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class WardView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'ward_number', 'ward_name', 'ward_type')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        ward = Ward.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(ward, request, view=self)
        serializer = WardSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = WardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class WardDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        ward = Ward.objects.get(id=id)
        serializer = WardSerializer(ward)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        ward = Ward.objects.get(id=id)
        serializer = WardSerializer(ward, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        ward = Ward.objects.get(id=id)
        ward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# ward patients

class WardPatientView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'ward', 'patient')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        ward = self.request.query_params.get('ward', None)
        ward_patient = WardPatient.objects.filter(ward=ward).order_by('-created_at')
        serializer = WardPatientSerializer(ward_patient, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WardPatientSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class WardPatientDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        ward_patient = WardPatient.objects.get(id=id)
        serializer = WardPatientSerializer(ward_patient)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        ward_patient = WardPatient.objects.get(id=id)
        serializer = WardPatientSerializer(ward_patient, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        ward_patient = WardPatient.objects.get(id=id)
        ward_patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class WardCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = WardCodeConfig.objects.get(id=id)
        serializer = WardCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = WardCodeConfig.objects.get(id=id)
        serializer = WardCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewWardCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = WardCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = WardCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        WardCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="WD",
            last_code="0000"
        )

# --------------------------------------------------------------------------------------
# dashboard

