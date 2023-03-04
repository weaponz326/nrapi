import datetime
import uuid

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

from .models import AccountUser, Access, Invitation
from .serializers import AccountUserSerializer, AccessSerializer, InvitationSerializer
from suites.hotel.accounts.models import Account
from suites.personal.users.paginations import TablePagination


# Create your views here.

# users

class AccountUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        user = AccountUser.objects.filter(account=account)
        serializer = AccountUserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountUserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AccountUserDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        user = AccountUser.objects.get(id=id)
        serializer = AccountUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        user = AccountUser.objects.get(id=id)
        serializer = AccountUserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        user = AccountUser.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# all accounts of an account belonging to a user
class AccountUserAccountView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        personal_id = self.request.query_params.get('personal_id', None)
        user = AccountUser.objects.filter(personal_user__id=personal_id)
        serializer = AccountUserSerializer(user, many=True)
        return Response(serializer.data)


# access
# ---------------------------------------------------------------------------

class AccessView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        access = Access.objects.filter(account=account)
        serializer = AccessSerializer(access, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class AccessDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        access = Access.objects.get(id=id)
        serializer = AccessSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Access.objects.get(id=id)
        serializer = AccessSerializer(access, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Access.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------------------------------------------------

class InvitationView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'invitee_name', 'invitation_status']
    ordering = ['-created_at']

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        invitation = Invitation.objects.filter(account=account)
        results = self.paginate_queryset(invitation, request, view=self)
        serializer = InvitationSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = InvitationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.id = request.data.get(id)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class InvitationDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        access = Invitation.objects.get(id=id)
        serializer = InvitationSerializer(access)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        access = Invitation.objects.get(id=id)
        serializer = InvitationSerializer(access, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        access = Invitation.objects.get(id=id)
        access.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def account_user_count(request):
    count = AccountUser.objects\
        .filter(account=request.query_params.get('account', None))\
        .count()            
    content = {'count': count}
    return Response(content)

# ------------------------------------------------------------------------------------------
# signals

@receiver(post_save, sender=Account)
def save_creator_user(sender, instance, created, **kwargs):
    if created:
        AccountUser.objects.create(
            account=Account.objects.get(id=instance.id),
            personal_user=instance.creator,
            is_creator=True,
            access_level="Admin",
        )

@receiver(post_save, sender=Invitation)
def save_invitation_user(sender, instance, created, **kwargs):
    if not created:
        if instance.invitation_status == 'Accepted':
            AccountUser.objects.create(
                account=Account.objects.get(id=uuid.UUID(str(instance.account))),
                personal_user=instance.user,
                access_level="Staff",
            )

@receiver(post_save, sender=AccountUser)
def save_access(sender, instance, created, **kwargs):
    if created:
        if instance.access_level == "Admin":
            Access.objects.create(
                id=instance.id,
                account=Account.objects.get(id=uuid.UUID(str(instance.account))),
                admin_access=True,
                portal_access=True,
                settings_access=True,
                bills_access=True,
                staff_access=True,
                roster_access=True,
                guests_access=True,
                payments_access=True,
                services_access=True,
                checkin_access=True,
                bookings_access=True,
                rooms_access=True,
                assets_access=True,
                housekeeping_access=True
            )
        else:
            Access.objects.create(
                id=instance.id,
                account=Account.objects.get(id=uuid.UUID(str(instance.account))),
                admin_access=False,
                portal_access=False,
                settings_access=False,
                bills_access=False,
                staff_access=False,
                roster_access=False,
                guests_access=False,
                payments_access=False,
                services_access=False,
                checkin_access=False,
                bookings_access=False,
                rooms_access=False,
                assets_access=False,
                housekeeping_access=False
            )
