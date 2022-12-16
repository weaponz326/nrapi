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

from .models import Leave 
from .serializers import LeaveSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates


# Create your views here.

class LeaveView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'leave_code', 'employee', 'leave_type', 'leave_status']
    ordering = ['-created_at']

    def get(self, request, format=None):
        leave = self.request.query_params.get('leave', None)
        account = Leave.objects.filter(account=leave).order_by('-created_at')
        results = self.paginate_queryset(account, request, view=self)
        serializer = LeaveSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = LeaveSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class LeaveDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        leave = Leave.objects.get(id=id)
        serializer = LeaveSerializer(leave)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        leave = Leave.objects.get(id=id)
        serializer = LeaveSerializer(leave, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        leave = Leave.objects.get(id=id)
        leave.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
