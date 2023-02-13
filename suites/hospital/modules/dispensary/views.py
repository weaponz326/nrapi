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

from .models import Dispense, DispenseCodeConfig, DispenseItem
from .serializers import DispenseCodeConfigSerializer, DispenseItemSerializer, DispenseSerializer
from suites.hospital.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class DispenseView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'dispense_code', 'dispense_date']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        dispense = Dispense.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(dispense, request, view=self)
        serializer = DispenseSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = DispenseSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DispenseDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        dispense = Dispense.objects.get(id=id)
        serializer = DispenseSerializer(dispense)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        dispense = Dispense.objects.get(id=id)
        serializer = DispenseSerializer(dispense, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        dispense = Dispense.objects.get(id=id)
        dispense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# dispense item

class DispenseItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        dispense = self.request.query_params.get('dispense', None)
        item = DispenseItem.objects.filter(dispense=dispense).order_by('created_at')
        serializer = DispenseItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # TODO:
        # insert into deliveries if dispense_type == delivery

        serializer = DispenseItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DispenseItemDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        item = DispenseItem.objects.get(id=id)
        serializer = DispenseItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = DispenseItem.objects.get(id=id)
        serializer = DispenseItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = DispenseItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class DispenseCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = DispenseCodeConfig.objects.get(id=id)
        serializer = DispenseCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = DispenseCodeConfig.objects.get(id=id)
        serializer = DispenseCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewDispenseCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = DispenseCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = DispenseCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        DispenseCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="DS",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def dispense_count(request):
    count = Dispense.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)
