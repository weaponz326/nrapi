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

from .models import Committee, CommitteeMember
from .serializers import CommitteeSerializer, CommitteeMemberSerializer
from suites.association.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class CommitteeView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'committee_code', 'committee_name')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        committee = Committee.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(committee, request, view=self)
        serializer = CommitteeSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CommitteeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CommitteeDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        committee = Committee.objects.get(id=id)
        serializer = CommitteeSerializer(committee)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        committee = Committee.objects.get(id=id)
        serializer = CommitteeSerializer(committee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        committee = Committee.objects.get(id=id)
        committee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# committee members

class CommitteeMemberView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'committee', 'member')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        committee = self.request.query_params.get('committee', None)
        committee_member = CommitteeMember.objects.filter(committee=committee).order_by('-created_at')
        serializer = CommitteeMemberSerializer(committee_member, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommitteeMemberSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CommitteeMemberDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        committee_member = CommitteeMember.objects.get(id=id)
        serializer = CommitteeMemberSerializer(committee_member)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        committee_member = CommitteeMember.objects.get(id=id)
        serializer = CommitteeMemberSerializer(committee_member, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        committee_member = CommitteeMember.objects.get(id=id)
        committee_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# dashboard

