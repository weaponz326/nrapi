import datetime
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import post_save

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from suites.enterprise.accounts.models import Account
from .models import Leave, LeaveCodeConfig 
from .serializers import LeaveCodeConfigSerializer, LeaveSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class LeaveView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'leave_code', 'employee', 'leave_type', 'leave_status']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        leave = Leave.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(leave, request, view=self)
        serializer = LeaveSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = LeaveSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class LeaveDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        leave = Leave.objects.get(id=id)
        serializer = LeaveSerializer(leave)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        leave = Leave.objects.get(id=id)
        serializer = LeaveSerializer(leave, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        leave = Leave.objects.get(id=id)
        leave.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class LeaveCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = LeaveCodeConfig.objects.get(id=id)
        serializer = LeaveCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = LeaveCodeConfig.objects.get(id=id)
        serializer = LeaveCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewLeaveCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = LeaveCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = LeaveCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        LeaveCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="LV",
            last_code="00000"
        )
