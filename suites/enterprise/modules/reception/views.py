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

from .models import Visitor 
from .serializers import VisitorSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates


# Create your views here.

class VisitorView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'visitor_code', 'visit_date', 'visitor_name', 'visitor_phone', 'tag_number']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        visitor = Visitor.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(visitor, request, view=self)
        serializer = VisitorSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = VisitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class VisitorDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        visitor = Visitor.objects.get(id=id)
        serializer = VisitorSerializer(visitor)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        visitor = Visitor.objects.get(id=id)
        serializer = VisitorSerializer(visitor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        visitor = Visitor.objects.get(id=id)
        visitor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
