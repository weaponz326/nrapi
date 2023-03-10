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

from suites.personal.users.services import generate_code, get_initials

from .models import Executive, ExecutiveCodeConfig
from .serializers import ExecutiveCodeConfigSerializer, ExecutiveSerializer
from suites.association.accounts.models import Account
from suites.personal.users.paginations import TablePagination


# Create your views here.


class ExecutiveView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'member')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        executive = Executive.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(executive, request, view=self)
        serializer = ExecutiveSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ExecutiveSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ExecutiveDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        executive = Executive.objects.get(id=id)
        serializer = ExecutiveSerializer(executive)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        executive = Executive.objects.get(id=id)
        serializer = ExecutiveSerializer(executive, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        executive = Executive.objects.get(id=id)
        executive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class ExecutiveCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = ExecutiveCodeConfig.objects.get(id=id)
        serializer = ExecutiveCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = ExecutiveCodeConfig.objects.get(id=id)
        serializer = ExecutiveCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewExecutiveCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = ExecutiveCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = ExecutiveCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        ExecutiveCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="EX",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

