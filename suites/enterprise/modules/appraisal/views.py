import datetime
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import Appraisal, AppraisalSheet 
from .serializers import AppraisalSerializer, AppraisalSheetSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates


# Create your views here.

class AppraisalView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'appraisal_code', 'employee', 'appraisal_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        appraisal = Appraisal.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(appraisal, request, view=self)
        serializer = AppraisalSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AppraisalSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AppraisalDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        appraisal = Appraisal.objects.get(id=id)
        serializer = AppraisalSerializer(appraisal)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        appraisal = Appraisal.objects.get(id=id)
        serializer = AppraisalSerializer(appraisal, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        appraisal = Appraisal.objects.get(id=id)
        appraisal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------
# appraisal sheet

class AppraisalSheetView(APIView, TablePagination):
    def get(self, request, format=None):
        appraisal = self.request.query_params.get('appraisal', None)
        sheet = AppraisalSheet.objects.filter(account=appraisal).order_by('-created_at')
        results = self.paginate_queryset(sheet, request, view=self)
        serializer = AppraisalSheetSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AppraisalSheetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AppraisalSheetDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        appraisal = AppraisalSheet.objects.get(id=id)
        serializer = AppraisalSheetSerializer(appraisal)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        appraisal = AppraisalSheet.objects.get(id=id)
        serializer = AppraisalSheetSerializer(appraisal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        appraisal = AppraisalSheet.objects.get(id=id)
        appraisal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Appraisal)
def save_appraisal_sheet(sender, instance, created, **kwargs):
    if created:
        AppraisalSheet.objects.create(
            id=instance.id,
        )