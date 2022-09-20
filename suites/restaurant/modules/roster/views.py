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
    RosterSheet
)
from .serializers import (
    RosterSerializer,
    ShiftSerializer,
    BatchSerializer,
    StaffPersonnelSerializer,
    RosterDaySerializer,
    RosterSheetSerializer
)
from modules.staff.models import Staff
from accounts.paginations import TablePagination


# Create your views here.

class RosterView(APIView, TablePagination):
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'roster_code', 'roster_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        roster = Roster.objects.filter(account=account)
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
        roster = Roster.objects.get(id=id)
        roster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------------------------------
# batches

class BatchView(APIView):
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
        roster = Batch.objects.get(id=id)
        roster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------
# personnel

class RefreshPersonnelView(APIView):
    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        roster_instance = Roster.objects.get(id=roster)
        account = roster_instance.account
        staff_set = Staff.objects.filter(account=account)

        for staff in staff_set:
            if not StaffPersonnel.objects.filter(roster=roster):
                personnel = StaffPersonnel(roster=roster_instance, staff=staff)
                personnel.save()

        return Response({ 'message' : 'OK' })

class StaffPersonnelView(APIView):
    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        personnel = StaffPersonnel.objects.filter(roster=roster)
        serializer = StaffPersonnelSerializer(personnel, many=True)
        return Response(serializer.data)

class StaffPersonnelDetailView(APIView):
    def put(self, request, id, format=None):
        personnel = Batch.objects.get(id=id)
        serializer = StaffPersonnelSerializer(personnel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        roster = Batch.objects.get(id=id)
        roster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------------------
# roster sheet

class RefreshSheetView(APIView):
    def get(self, request, format=None):

        def daterange(from_date, to_date):
            for n in range(int((to_date - from_date).days)):
                yield from_date + timedelta(n)

        roster = self.request.query_params.get('roster', None)
        roster_instance = Roster.objects.get(id=roster)

    	# fill days table
        from_date = roster_instance.from_date
        to_date = roster_instance.to_date

        add_list = []
        delete_list = []
        day_set = RosterDay.objects.filter(roster=roster)

        if day_set.exists():
            for new_day in daterange(from_date, to_date):
                for day in day_set.iterator():
                    if (new_day != day) and (new_day > to_date):
                        add_list.append(RosterDay(roster=roster_instance, day=str(new_day)))
                    if (new_day != day) and (new_day < from_date):
                        delete_list.append({roster:roster_instance, day:day})

            if not add_list == []: RosterDay.objects.bulk_create(add_list)
            if not delete_list == []: RosterDay.objects.filter(roster__in=delete_list[roster], day__in=delete_list[day])
        else:
            for new_day in daterange(from_date, to_date):
                add_list.append(RosterDay(roster=roster_instance, day=str(new_day)))
            if not add_list == []: RosterDay.objects.bulk_create(add_list)

        return Response({ 'message' : 'OK' })

class RosterDayView(APIView):
    def get(self, request, format=None):
        roster = self.request.query_params.get('roster', None)
        day = RosterDay.objects.filter(roster=roster)
        serializer = RosterDaySerializer(day, many=True)
        return Response(serializer.data)

# TODO: insert and get sheet batches
class RosterSheetView(APIView):
    def get(self, request, format=None):
        return Response({ 'message' : 'TODO' })

    def post(self, request, format=None):
        return Response({ 'message' : 'TODO' })

# -----------------------------------------------------------------------------------

@receiver(post_save, sender=Shift)
def save_sheet(sender, instance, created, **kwargs):
    shifts = Shift.objects.filter(roster=instance.roster)
    days = get_roster_days(instance.from_date, instance.to_date)

    if created:
        for s in shifts:
            RosterSheet.objects.create(
                roster=instance.roster,
                shift=s.shift_name, 
                days=days
            )

    if not created:
        pass

def get_roster_days(from_date, to_date):
    date_batch_objects = {}
    delta = date(to_date) - date(from_date)

    for i in range(delta.days + 1):
        day = from_date + timedelta(days=i)
        data = {day: ''}
        data = json.load(data)
        date_batch_objects.update(data)

    print(date_batch_objects)
    return date_batch_objects
    
# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def roster_count(request):
    count = Roster.objects\
        .filter(account=request.query_params.get('account', None))\
        .count()            
    content = {'count': count}
    return Response(content)
