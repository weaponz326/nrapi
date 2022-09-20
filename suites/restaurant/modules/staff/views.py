from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.decorators import api_view

from .models import Staff
from .serializers import StaffSerializer
from suites.personal.users.paginations import TablePagination


# Create your views here.

class StaffView(APIView, TablePagination):
    parser_class = (FileUploadParser,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'staff_code', 'first_name', 'last_name', 'department', 'job']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        staff = Staff.objects.filter(account=account)
        results = self.paginate_queryset(staff, request, view=self)
        serializer = StaffSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class StaffDetailView(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request, id, format=None):
        staff = Staff.objects.get(id=id)
        serializer = StaffSerializer(staff)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        staff = Staff.objects.get(id=id)
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        staff = Staff.objects.get(id=id)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def staff_count(request):
    count = Staff.objects\
        .filter(account=request.query_params.get('account', None))\
        .count()            
    content = {'count': count}
    return Response(content)
