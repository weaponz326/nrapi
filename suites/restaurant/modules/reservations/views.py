import datetime
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import Reservation, ReservationTable
from .serializers import ReservationDepthSerializer, ReservationSerializer, ReservationTableDepthSerializer, ReservationTableSerializer
from accounts.paginations import TablePagination
from accounts.services import fillZeroDates


# Create your views here.

class ReservationView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'resrevation_code', 'reservation_date', 'customer_name', 'arrival_date', 'reservation_status']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        reservation = Reservation.objects.filter(account=account)
        results = self.paginate_queryset(reservation, request, view=self)
        serializer = ReservationSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ReservationDetailView(APIView):
    def get(self, request, id, format=None):
        reservation = Reservation.objects.get(id=id)
        serializer = ReservationDepthSerializer(reservation)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        reservation = Reservation.objects.get(id=id)
        serializer = ReservationSerializer(reservation, data=request.data)
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
    def get(self, request, format=None):
        reservation = self.request.query_params.get('account', None)
        reservation_table = ReservationTable.objects.filter(reservation=reservation)
        serializer = ReservationTableDepthSerializer(reservation_table, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationTableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ReservationTableDetailView(APIView):
    def get(self, request, id, format=None):
        reservation_table = ReservationTable.objects.get(id=id)
        serializer = ReservationTableDepthSerializer(reservation_table)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        reservation_table = ReservationTable.objects.get(id=id)
        serializer = ReservationSerializer(reservation_table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        reservation_table = ReservationTable.objects.get(id=id)
        reservation_table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
    filled_items = fillZeroDates(items)
    return Response(filled_items)
