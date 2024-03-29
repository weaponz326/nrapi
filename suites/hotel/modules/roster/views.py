from datetime import date, timedelta, datetime
import json

from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view


from .models import (
    Roster,
    Shift,
    Batch,
    StaffPersonnel,
    RosterDay,
    RosterCodeConfig,
)
from .serializers import (
    RosterSerializer,
    ShiftSerializer,
    BatchSerializer,
    StaffPersonnelSerializer,
    RosterDaySerializer,
    RosterCodeConfigSerializer,
)
from suites.hotel.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class RosterView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'roster_code', 'roster_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        roster = Roster.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(roster, request, view=self)
        serializer = RosterSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = RosterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class RosterDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        roster = Roster.objects.get(id=id)
        serializer = RosterSerializer(roster)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        roster = Roster.objects.get(id=id)
        serializer = RosterSerializer(roster, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        roster = Roster.objects.get(id=id)
        roster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------------------------
# shifts

class ShiftView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        shift = Shift.objects.filter(roster=roster)
        serializer = ShiftSerializer(shift, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ShiftDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        shift = Shift.objects.get(id=id)
        serializer = ShiftSerializer(shift)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        shift = Shift.objects.get(id=id)
        serializer = ShiftSerializer(shift, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        shift = Shift.objects.get(id=id)
        shift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------------------------
# batches

class BatchView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        batch = Batch.objects.filter(roster=roster)
        serializer = BatchSerializer(batch, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BatchDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        batch = Batch.objects.get(id=id)
        serializer = BatchSerializer(batch)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        batch = Batch.objects.get(id=id)
        serializer = BatchSerializer(batch, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        batch = Batch.objects.get(id=id)
        batch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------
# personnel

class StaffPersonnelView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        personnel = StaffPersonnel.objects.filter(roster=roster)
        serializer = StaffPersonnelSerializer(personnel, many=True)
        return Response(serializer.data)

class StaffPersonnelDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def put(self, request, id, format=None):
        personnel = Batch.objects.get(id=id)
        serializer = StaffPersonnelSerializer(personnel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        personnel = StaffPersonnel.objects.get(id=id)
        personnel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------------------
# roster day

class RosterDayView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        roster_day = RosterDay.objects.filter(roster=roster)
        serializer = RosterDaySerializer(roster_day, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RosterDaySerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class RosterDayDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        roster_day = RosterDay.objects.get(id=id)
        serializer = RosterDaySerializer(roster_day)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        roster_day = RosterDay.objects.get(id=id)
        serializer = RosterDaySerializer(roster_day, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        roster_day = RosterDay.objects.get(id=id)
        roster_day.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# --------------------------------------------------------------------------------------
# config

class RosterCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = RosterCodeConfig.objects.get(id=id)
        serializer = RosterCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = RosterCodeConfig.objects.get(id=id)
        serializer = RosterCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewRosterCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = RosterCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = RosterCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        RosterCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="RT",
            last_code="000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def roster_count(request):
    count = Roster.objects\
        .filter(account=request.query_params.get('account', None))\
        .count()            
    content = {'count': count}
    return Response(content)
