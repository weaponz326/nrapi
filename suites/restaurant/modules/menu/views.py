from django.shortcuts import render
from django.db.models import Count

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.decorators import api_view

from .models import MenuGroup, MenuItem
from .serializers import  MenuGroupSerializer, MenuItemSerializer
from suites.personal.users.paginations import TablePagination


# Create your views here.

class MenuGroupView(APIView, TablePagination):
    parser_class = (FileUploadParser,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'menu_group', 'category']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        menu_group = MenuGroup.objects.filter(account=account)
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
    parser_classes = (MultiPartParser,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'item_code', 'item_name', 'price', 'menu_group.menu_group', 'menu_group.category']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        menu_item = MenuItem.objects.filter(menu_group__account=account)
        results = self.paginate_queryset(menu_item, request, view=self)
        serializer = MenuItemSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

class MenuItemView(APIView):
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