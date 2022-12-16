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

from .models import ReceivedLetter, SentLetter 
from .serializers import ReceivedLetterSerializer, SentLetterSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates


# Create your views here.

# sent letter

class SentLetterView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'date_sent', 'reference_number', 'subject', 'recepient']
    ordering = ['-created_at']

    def get(self, request, format=None):
        sent_letter = self.request.query_params.get('sent_letter', None)
        account = SentLetter.objects.filter(account=sent_letter).order_by('-created_at')
        results = self.paginate_queryset(account, request, view=self)
        serializer = SentLetterSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = SentLetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class SentLetterDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        sent_letter = SentLetter.objects.get(id=id)
        serializer = SentLetterSerializer(sent_letter)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        sent_letter = SentLetter.objects.get(id=id)
        serializer = SentLetterSerializer(sent_letter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        sent_letter = SentLetter.objects.get(id=id)
        sent_letter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# received letter

class ReceivedLetterView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'date_received', 'reference_number', 'subject', 'recepient']
    ordering = ['-created_at']

    def get(self, request, format=None):
        received_letter = self.request.query_params.get('received_letter', None)
        account = ReceivedLetter.objects.filter(account=received_letter).order_by('-created_at')
        results = self.paginate_queryset(account, request, view=self)
        serializer = ReceivedLetterSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ReceivedLetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ReceivedLetterDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        received_letter = ReceivedLetter.objects.get(id=id)
        serializer = ReceivedLetterSerializer(received_letter)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        received_letter = ReceivedLetter.objects.get(id=id)
        serializer = ReceivedLetterSerializer(received_letter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        received_letter = ReceivedLetter.objects.get(id=id)
        received_letter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
