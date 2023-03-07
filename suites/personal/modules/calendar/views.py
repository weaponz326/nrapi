import datetime
from django.dispatch import receiver
from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.db.models.signals import post_save

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from suites.personal.users.models import User
from .models import Calendar, CalendarCodeConfig, Schedule, ScheduleCodeConfig
from .serializers import CalendarCodeConfigSerializer, CalendarSerializer, ScheduleCodeConfigSerializer, ScheduleSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class CalendarView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['calendar_name', 'created_at']
    ordering = ['-created_at']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        calendar = Calendar.objects.filter(user=user).order_by('-created_at')
        results = self.paginate_queryset(calendar, request, view=self)
        serializer = CalendarSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CalendarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CalendarDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        access = Calendar.objects.get(id=id)
        serializer = CalendarSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Calendar.objects.get(id=id)
        serializer = CalendarSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Calendar.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------------------------------
# schedule

class AllScheduleView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)

    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'schedule_name', 'calendar', 'start_date', 'end_date', 'status']
    ordering = ['-created_at']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        schedule = Schedule.objects.filter(calendar__user=user).order_by('-created_at')
        results = self.paginate_queryset(schedule, request, view=self)
        serializer = ScheduleSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

class ScheduleView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        calendar = self.request.query_params.get('calendar', None)
        schedule = Schedule.objects.filter(calendar=calendar)
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScheduleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ScheduleDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        access = Schedule.objects.get(id=id)
        serializer = ScheduleSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Schedule.objects.get(id=id)
        serializer = ScheduleSerializer(access, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Schedule.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

# calendar

class CalendarCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = CalendarCodeConfig.objects.get(id=id)
        serializer = CalendarCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = CalendarCodeConfig.objects.get(id=id)
        serializer = CalendarCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewCalendarCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = CalendarCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = CalendarCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=User)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        CalendarCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.first_name) + get_initials(instance.last_name),
            suffix="CA",
            last_code="0000"
        )

# schedule

class ScheduleCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = ScheduleCodeConfig.objects.get(id=id)
        serializer = ScheduleCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = ScheduleCodeConfig.objects.get(id=id)
        serializer = ScheduleCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewScheduleCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = ScheduleCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = ScheduleCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=User)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        ScheduleCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.first_name) + get_initials(instance.last_name),
            suffix="SD",
            last_code="000000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def calendar_count(request):
    count = Calendar.objects\
        .filter(user__id=request.query_params.get('user', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()            
    content = {'count': count}
    return Response(content)

@api_view()
def schedule_count(request):
    count = Schedule.objects\
        .filter(calendar__user__id=request.query_params.get('user', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()            
    content = {'count': count}
    return Response(content)

@api_view()
def calendar_annotate(request):
    items = Calendar.objects\
        .filter(user__id=request.query_params.get('user', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_items = fiil_zero_dates(items)
    return Response(filled_items)

@api_view()
def schedule_annotate(request):
    items = Schedule.objects\
        .filter(calendar__user__id=request.query_params.get('user', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_items = fiil_zero_dates(items)
    return Response(filled_items)

