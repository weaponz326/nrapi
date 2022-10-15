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

from .models import Timetable, TimetableCodeConfig, TimetableClass, TimetablePeriod
from .serializers import TimetableCodeConfigSerializer, TimetablePeriodSerializer, TimetableSerializer, TimetableClassSerializer
from suites.restaurant.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class TimetableView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'timetable_code', 'timetable_name')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        timetable = Timetable.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(timetable, request, view=self)
        serializer = TimetableSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TimetableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TimetableDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        timetable = Timetable.objects.get(id=id)
        serializer = TimetableSerializer(timetable)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        timetable = Timetable.objects.get(id=id)
        serializer = TimetableSerializer(timetable, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        timetable = Timetable.objects.get(id=id)
        timetable.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# timetable classes

class TimetableClassView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'timetable', 'clase')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        timetable = self.request.query_params.get('timetable', None)
        timetable_class = TimetableClass.objects.filter(timetable=timetable).order_by('-created_at')
        results = self.paginate_queryset(timetable_class, request, view=self)
        serializer = TimetableClassSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TimetableClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TimetableClassDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        timetable_class = TimetableClass.objects.get(id=id)
        serializer = TimetableClassSerializer(timetable_class)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        timetable_class = TimetableClass.objects.get(id=id)
        serializer = TimetableClassSerializer(timetable_class, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        timetable_class = TimetableClass.objects.get(id=id)
        timetable_class.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# timetable periods

class TimetablePeriodView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'timetable', 'period', 'period_start', 'period_end')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        timetable = self.request.query_params.get('timetable', None)
        timetable_period = TimetablePeriod.objects.filter(timetable=timetable).order_by('-created_at')
        results = self.paginate_queryset(timetable_period, request, view=self)
        serializer = TimetablePeriodSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TimetablePeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TimetablePeriodDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        timetable_period = TimetablePeriod.objects.get(id=id)
        serializer = TimetablePeriodSerializer(timetable_period)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        timetable_period = TimetablePeriod.objects.get(id=id)
        serializer = TimetablePeriodSerializer(timetable_period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        timetable_period = TimetablePeriod.objects.get(id=id)
        timetable_period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# timetable sheet

# TODO:

# --------------------------------------------------------------------------------------
# config

class TimetableCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = TimetableCodeConfig.objects.get(id=id)
        serializer = TimetableCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = TimetableCodeConfig.objects.get(id=id)
        serializer = TimetableCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewTimetableCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = TimetableCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = TimetableCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        TimetableCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="TT",
            last_code="0000"
        )

# --------------------------------------------------------------------------------------
# dashboard

