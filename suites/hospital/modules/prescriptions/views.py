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

from .models import Prescription, PrescriptionCodeConfig, PrescriptionItem
from .serializers import PrescriptionCodeConfigSerializer, PrescriptionItemSerializer, PrescriptionSerializer
from suites.hospital.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class PrescriptionView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'prescription_code', 'prescription_date']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        prescription = Prescription.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(prescription, request, view=self)
        serializer = PrescriptionSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PrescriptionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PrescriptionDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        prescription = Prescription.objects.get(id=id)
        serializer = PrescriptionSerializer(prescription)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        prescription = Prescription.objects.get(id=id)
        serializer = PrescriptionSerializer(prescription, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        prescription = Prescription.objects.get(id=id)
        prescription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# prescription item

class PrescriptionItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        prescription = self.request.query_params.get('prescription', None)
        item = PrescriptionItem.objects.filter(prescription=prescription).order_by('created_at')
        serializer = PrescriptionItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # TODO:
        # insert into deliveries if prescription_type == delivery

        serializer = PrescriptionItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PrescriptionItemDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        item = PrescriptionItem.objects.get(id=id)
        serializer = PrescriptionItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = PrescriptionItem.objects.get(id=id)
        serializer = PrescriptionItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = PrescriptionItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class PrescriptionCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = PrescriptionCodeConfig.objects.get(id=id)
        serializer = PrescriptionCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = PrescriptionCodeConfig.objects.get(id=id)
        serializer = PrescriptionCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewPrescriptionCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = PrescriptionCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = PrescriptionCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        PrescriptionCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="PR",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def prescription_count(request):
    count = Prescription.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)
