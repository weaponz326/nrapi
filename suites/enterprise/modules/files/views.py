import datetime
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.db.models import Sum

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import File, Folder 
from .serializers import FileSerializer, FolderSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates


# Create your views here.

# folders

class FolderView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'folder_number', 'folder_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        folder = Folder.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(folder, request, view=self)
        serializer = FolderSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = FolderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class FolderDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        folder = Folder.objects.get(id=id)
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        folder = Folder.objects.get(id=id)
        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        folder = Folder.objects.get(id=id)
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------
# files

class FileView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'file_number', 'file_name', 'file_type', 'date_added']
    ordering = ['-created_at']

    def get(self, request, format=None):
        folder = self.request.query_params.get('folder', None)
        file = File.objects.filter(folder=folder).order_by('-created_at')
        results = self.paginate_queryset(file, request, view=self)
        serializer = FileSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class FileDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        file = File.objects.get(id=id)
        serializer = FileSerializer(file)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        file = File.objects.get(id=id)
        serializer = FileSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        file = File.objects.get(id=id)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
