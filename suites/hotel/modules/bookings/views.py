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

from .models import Booking, BookingCodeConfig, BookedRoom
from .serializers import BookingCodeConfigSerializer, BookingSerializer, BookedRoomSerializer
from suites.hotel.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class BookingView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'booking_code', 'booking_date', 'customer_name', 'booking_type', 'total_amount']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        booking = Booking.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(booking, request, view=self)
        serializer = BookingSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BookingDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        booking = Booking.objects.get(id=id)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        booking = Booking.objects.get(id=id)
        serializer = BookingSerializer(booking, data=request.data, context={'request': request}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        booking = Booking.objects.get(id=id)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ----------------------------------------------------------------------------------------------------------
# booking item

class BookedRoomView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        booking = self.request.query_params.get('booking', None)
        item = BookedRoom.objects.filter(booking=booking).order_by('created_at')
        serializer = BookedRoomSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # TODO:
        # insert into deliveries if booking_type == delivery

        serializer = BookedRoomSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BookedRoomDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        item = BookedRoom.objects.get(id=id)
        serializer = BookedRoomSerializer(item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        item = BookedRoom.objects.get(id=id)
        serializer = BookedRoomSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        item = BookedRoom.objects.get(id=id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class BookingCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = BookingCodeConfig.objects.get(id=id)
        serializer = BookingCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = BookingCodeConfig.objects.get(id=id)
        serializer = BookingCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewBookingCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = BookingCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = BookingCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        BookingCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="BK",
            last_code="00000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def booking_count(request):
    count = Booking.objects\
        .filter(account=request.query_params.get('account', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def booking_annotate(request):
    items = Booking.objects\
        .filter(account=request.query_params.get('account', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_items = fiil_zero_dates(items)
    return Response(filled_items)
