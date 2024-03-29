import datetime
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import Reservation, ReservationCodeConfig, ReservationTable
from .serializers import ReservationCodeConfigSerializer, ReservationSerializer, ReservationTableSerializer
from suites.restaurant.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class ReservationView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'resrevation_code', 'reservation_date', 'customer_name', 'arrival_date', 'reservation_status']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        reservation = Reservation.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(reservation, request, view=self)
        serializer = ReservationSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ReservationDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        reservation = Reservation.objects.get(id=id)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        reservation = Reservation.objects.get(id=id)
        serializer = ReservationSerializer(reservation, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        reservation = Reservation.objects.get(id=id)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------
# reservations

class ReservationTableView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        reservation = self.request.query_params.get('account', None)
        reservation_table = ReservationTable.objects.filter(reservation=reservation).order_by('-created_at')
        serializer = ReservationTableSerializer(reservation_table, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationTableSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ReservationTableDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        reservation_table = ReservationTable.objects.get(id=id)
        serializer = ReservationTableSerializer(reservation_table)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        reservation_table = ReservationTable.objects.get(id=id)
        serializer = ReservationSerializer(reservation_table, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        reservation_table = ReservationTable.objects.get(id=id)
        reservation_table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class ReservationCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = ReservationCodeConfig.objects.get(id=id)
        serializer = ReservationCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = ReservationCodeConfig.objects.get(id=id)
        serializer = ReservationCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewReservationCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = ReservationCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = ReservationCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        ReservationCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="RE",
            last_code="0000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def reservation_count(request):
    count = Reservation.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def reservation_annotate(request):
    items = Reservation.objects\
        .filter(account=request.query_params.get('account', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_items = fiil_zero_dates(items)
    return Response(filled_items)
