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

from .models import Group, GroupCodeConfig, GroupMember
from .serializers import GroupCodeConfigSerializer, GroupSerializer, GroupMemberSerializer
from suites.association.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class GroupView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'group_code', 'group_name')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        group = Group.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(group, request, view=self)
        serializer = GroupSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class GroupDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        group = Group.objects.get(id=id)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        group = Group.objects.get(id=id)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        group = Group.objects.get(id=id)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# group members

class GroupMemberView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter,]
    ordering_fields = ('created_at', 'group', 'member')
    ordering = ('-created_at',)

    def get(self, request, format=None):
        group = self.request.query_params.get('group', None)
        group_member = GroupMember.objects.filter(group=group).order_by('-created_at')
        serializer = GroupMemberSerializer(group_member, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupMemberSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class GroupMemberDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        group_member = GroupMember.objects.get(id=id)
        serializer = GroupMemberSerializer(group_member)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        group_member = GroupMember.objects.get(id=id)
        serializer = GroupMemberSerializer(group_member, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        group_member = GroupMember.objects.get(id=id)
        group_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class GroupCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = GroupCodeConfig.objects.get(id=id)
        serializer = GroupCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = GroupCodeConfig.objects.get(id=id)
        serializer = GroupCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewGroupCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = GroupCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = GroupCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        GroupCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="GP",
            last_code="0000"
        )

# --------------------------------------------------------------------------------------
# dashboard

