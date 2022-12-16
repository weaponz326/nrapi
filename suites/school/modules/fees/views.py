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

from .models import Fees, FeesCodeConfig, FeesTarget
from .serializers import FeesCodeConfigSerializer, FeesSerializer, FeesTargetSerializer
from suites.school.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class FeesView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'fees_code', 'fees_name', 'fees_date')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        fees = Fees.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(fees, request, view=self)
        serializer = FeesSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = FeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class FeesDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        fees = Fees.objects.get(id=id)
        serializer = FeesSerializer(fees)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        fees = Fees.objects.get(id=id)
        serializer = FeesSerializer(fees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        fees = Fees.objects.get(id=id)
        fees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# fees target

class FeesTargetView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'fees', 'clase')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        fees = self.request.query_params.get('fees', None)
        fees_target = FeesTarget.objects.filter(fees=fees).order_by('-created_at')
        serializer = FeesTargetSerializer(fees_target, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeesTargetSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class FeesTargetDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        fees = FeesTarget.objects.get(id=id)
        serializer = FeesTargetSerializer(fees)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        fees = Fees.objects.get(id=id)
        serializer = FeesTargetSerializer(fees, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        fees = Fees.objects.get(id=id)
        fees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class FeesCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = FeesCodeConfig.objects.get(id=id)
        serializer = FeesCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = FeesCodeConfig.objects.get(id=id)
        serializer = FeesCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewFeesCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = FeesCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = FeesCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        FeesCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="FE",
            last_code="0000"
        )

# --------------------------------------------------------------------------------------
# dashboard

