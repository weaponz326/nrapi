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

from .models import Parent, ParentCodeConfig, ParentWard
from .serializers import ParentCodeConfigSerializer, ParentSerializer, ParentWardSerializer
from suites.restaurant.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class ParentView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'parent_code', 'first_name', 'last_name', 'phone')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        parent = Parent.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(parent, request, view=self)
        serializer = ParentSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ParentDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        parent = Parent.objects.get(id=id)
        serializer = ParentSerializer(parent)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        parent = Parent.objects.get(id=id)
        serializer = ParentSerializer(parent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        parent = Parent.objects.get(id=id)
        parent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# parent wards

class ParentWardView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'parent', 'ward')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        parent = self.request.query_params.get('parent', None)
        parent_ward = ParentWard.objects.filter(parent=parent).order_by('-created_at')
        results = self.paginate_queryset(parent_ward, request, view=self)
        serializer = ParentWardSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ParentWardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ParentWardDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        parent_ward = ParentWard.objects.get(id=id)
        serializer = ParentWardSerializer(parent_ward)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        parent_ward = ParentWard.objects.get(id=id)
        serializer = ParentWardSerializer(parent_ward, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        parent_ward = ParentWard.objects.get(id=id)
        parent_ward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class ParentCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = ParentCodeConfig.objects.get(id=id)
        serializer = ParentCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = ParentCodeConfig.objects.get(id=id)
        serializer = ParentCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewParentCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = ParentCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = ParentCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        ParentCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="PT",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

