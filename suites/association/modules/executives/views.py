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

from .models import Executive
from .serializers import ExecutiveSerializer
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
        serializer = ExecutiveSerializer(executive, many=True)        
        return Response(serializer.data)

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
# dashboard

