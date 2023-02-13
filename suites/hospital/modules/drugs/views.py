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

from .models import Drug, DrugCodeConfig
from .serializers import DrugCodeConfigSerializer, DrugSerializer
from suites.hospital.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class DrugView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'ndc_number', 'drug_name', 'drug_status']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        drug = Drug.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(drug, request, view=self)
        serializer = DrugSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DrugSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DrugDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        drug = Drug.objects.get(id=id)
        serializer = DrugSerializer(drug)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        drug = Drug.objects.get(id=id)
        serializer = DrugSerializer(drug, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        drug = Drug.objects.get(id=id)
        drug.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class DrugCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = DrugCodeConfig.objects.get(id=id)
        serializer = DrugCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = DrugCodeConfig.objects.get(id=id)
        serializer = DrugCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewDrugCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = DrugCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = DrugCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        DrugCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="DG",
            last_code="0000000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def drug_count(request):
    count = Drug.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)
