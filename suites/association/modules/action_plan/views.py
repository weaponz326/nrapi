import datetime
from django.shortcuts import render
from django.db.models import Sum

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from .models import ActionPlan, PlanStep
from .serializers import ActionPlanSerializer, PlanStepSerializer
from suites.personal.users.paginations import TablePagination


# Create your views here.

class ActionPlanView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'plan_code', 'plan_title', 'plan_date']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        action_plan = ActionPlan.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(action_plan, request, view=self)
        serializer = ActionPlanSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ActionPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ActionPlanDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        action_plan = ActionPlan.objects.get(id=id)
        serializer = ActionPlanSerializer(action_plan)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        action_plan = ActionPlan.objects.get(id=id)
        serializer = ActionPlanSerializer(action_plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        action_plan = ActionPlan.objects.get(id=id)
        action_plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# plan steps
# --------------------------------------------------------------------------------------------------

class PlanStepView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        action_plan = self.request.query_params.get('action_plan', None)
        step = PlanStep.objects.filter(action_plan=action_plan).order_by('created_at')
        serializer = PlanStepSerializer(step, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PlanStepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class PlanStepDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        step = PlanStep.objects.get(id=id)
        serializer = PlanStepSerializer(step)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        step = PlanStep.objects.get(id=id)
        serializer = PlanStepSerializer(step, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        step = PlanStep.objects.get(id=id)
        step.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# dashboard
