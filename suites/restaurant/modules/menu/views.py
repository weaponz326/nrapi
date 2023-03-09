from django.shortcuts import render
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.decorators import api_view

from .models import MenuGroup, MenuGroupCodeConfig, MenuItem, MenuItemCodeConfig
from .serializers import  MenuGroupCodeConfigSerializer, MenuGroupSerializer, MenuItemSerializer, MenuItemCodeConfigSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials
from suites.restaurant.accounts.models import Account


# Create your views here.

class MenuGroupView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    parser_class = (FileUploadParser,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'menu_group', 'category']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        menu_group = MenuGroup.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(menu_group, request, view=self)
        serializer = MenuGroupSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class MenuGroupDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_class = (FileUploadParser,)

    def get(self, request, id, format=None):
        menu_group = MenuGroup.objects.get(id=id)
        serializer = MenuGroupSerializer(menu_group)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        menu_group = MenuGroup.objects.get(id=id)
        serializer = MenuGroupSerializer(menu_group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        menu_group = MenuGroup.objects.get(id=id)
        menu_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------
# menu items

class AllMenuItemView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'item_code', 'item_name', 'price', 'menu_group.menu_group', 'menu_group.category']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        menu_item = MenuItem.objects.filter(menu_group__account=account).order_by('-created_at')
        results = self.paginate_queryset(menu_item, request, view=self)
        serializer = MenuItemSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

class MenuItemView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        menu_group = self.request.query_params.get('menu_group', None)
        item = MenuItem.objects.filter(menu_group=menu_group)
        serializer = MenuItemSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class MenuItemDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        item = MenuItem.objects.get(id=id)
        serializer = MenuItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = MenuItem.objects.get(id=id)
        serializer = MenuItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = MenuItem.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class MenuGroupCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = MenuGroupCodeConfig.objects.get(id=id)
        serializer = MenuGroupCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = MenuGroupCodeConfig.objects.get(id=id)
        serializer = MenuGroupCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewMenuGroupCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = MenuGroupCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = MenuGroupCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        MenuGroupCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="MG",
            last_code="000"
        )

class MenuItemCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = MenuItemCodeConfig.objects.get(id=id)
        serializer = MenuItemCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = MenuItemCodeConfig.objects.get(id=id)
        serializer = MenuItemCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewMenuItemCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = MenuItemCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = MenuItemCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        MenuItemCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="MI",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def menu_group_count(request):
    count = MenuGroup.objects\
        .filter(account=request.query_params.get('account', None))\
        .count()            
    content = {'count': count}
    return Response(content)

@api_view()
def menu_item_count(request):
    count = MenuItem.objects\
        .filter(menu_group__account=request.query_params.get('account', None))\
        .count()            
    content = {'count': count}
    return Response(content)