from functools import partial
from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

from .models import ExtendedProfile
from .serializers import ExtendedProfileSerializer, InvitationSerializer
from suites.personal.users.models import User
from suites.personal.users.paginations import TablePagination


# Create your views here.

class ExtendedProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        profile = ExtendedProfile.objects.filter(user=user)
        serializer = ExtendedProfileSerializer(profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExtendedProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ExtendedProfileDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        extended_profile = ExtendedProfile.objects.get(id=id)
        serializer = ExtendedProfileSerializer(extended_profile)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        extended_profile = ExtendedProfile.objects.get(id=id)
        serializer = ExtendedProfileSerializer(extended_profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        extended_profile = ExtendedProfile.objects.get(id=id)
        extended_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=User)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        ExtendedProfile.objects.create(id=instance.id)

# ------------------------------------------------------------------------------------------
# invitations

class InvitationView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['subject', 'created_at', 'inviter', 'inviter_type', 'invitation_status']
    ordering = ['-created_at']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        Invitation = Invitation.objects.filter(user=user)
        results = self.paginate_queryset(Invitation, request, view=self)
        serializer = InvitationSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = InvitationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class InvitationDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, id, format=None):
        Invitation = Invitation.objects.get(id=id)
        serializer = InvitationSerializer(Invitation)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Invitation = Invitation.objects.get(id=id)
        serializer = InvitationSerializer(Invitation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        Invitation = Invitation.objects.get(id=id)
        Invitation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
