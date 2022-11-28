import datetime

from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.decorators import api_view

from .models import Member, MemberCodeConfig
from .serializers import MemberCodeConfigSerializer, MemberSerializer
from suites.association.accounts.models import Account
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import generate_code, get_initials


# Create your views here.

class MemberView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    parser_class = (FileUploadParser,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'member_code', 'first_name', 'last_name']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        member = Member.objects.filter(account=account).order_by('-created_at')
        results = self.paginate_queryset(member, request, view=self)
        serializer = MemberSerializer(results, many=True)        
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = MemberSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class MemberDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_class = (FileUploadParser,)

    def get(self, request, id, format=None):
        member = Member.objects.get(id=id)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        member = Member.objects.get(id=id)
        serializer = MemberSerializer(member, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        member = Member.objects.get(id=id)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

class MemberCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = MemberCodeConfig.objects.get(id=id)
        serializer = MemberCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = MemberCodeConfig.objects.get(id=id)
        serializer = MemberCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewMemberCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = MemberCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)        

        if code_set.entry_mode == 'Auto':
            code = MemberCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}{}'.format(code_set.prefix, new_code, code_set.year_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        MemberCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.name),
            suffix="ST",
            last_code="00000",
            year_code=datetime.datetime.now().strftime("%y")
        )

# --------------------------------------------------------------------------------------
# dashboard
