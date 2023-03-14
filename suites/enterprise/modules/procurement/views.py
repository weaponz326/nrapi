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

from suites.enterprise.accounts.models import Account
from .models import OrderReview, Procurement, ProcurementCodeConfig 
from .serializers import OrderReviewSerializer, ProcurementCodeConfigSerializer, ProcurementSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class ProcurementView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'procurement_code', 'vendor_name', 'order_code', 'order_date', 'order_status']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        procurement = Procurement.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(procurement, request, view=self)
        serializer = ProcurementSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ProcurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ProcurementDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        procurement = Procurement.objects.get(id=id)
        serializer = ProcurementSerializer(procurement)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        procurement = Procurement.objects.get(id=id)
        serializer = ProcurementSerializer(procurement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        procurement = Procurement.objects.get(id=id)
        procurement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------------
# order review

class OrderReviewView(APIView, TablePagination):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        order_review = OrderReview.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(order_review, request, view=self)
        serializer = OrderReviewSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = OrderReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class OrderReviewDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        order_review = OrderReview.objects.get(id=id)
        serializer = OrderReviewSerializer(order_review)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        order_review = OrderReview.objects.get(id=id)
        serializer = OrderReviewSerializer(order_review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        order_review = OrderReview.objects.get(id=id)
        order_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Procurement)
def save_order_review(sender, instance, created, **kwargs):
    if created:
        OrderReview.objects.create(
            id=instance.id,
        )

# --------------------------------------------------------------------------------------
# config

class ProcurementCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = ProcurementCodeConfig.objects.get(id=id)
        serializer = ProcurementCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = ProcurementCodeConfig.objects.get(id=id)
        serializer = ProcurementCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewProcurementCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = ProcurementCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = ProcurementCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        ProcurementCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="PR",
            last_code="00000"
        )
