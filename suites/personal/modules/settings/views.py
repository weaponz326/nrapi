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
from rest_framework.decorators import api_view

from .models import ExtendedProfile
from .serializers import ExtendedProfileSerializer
from suites.personal.users.models import User
from suites.personal.users.paginations import TablePagination

# from suites.restaurant.modules.admin.models import AccountUser, Invitation
# from suites.restaurant.modules.admin.serializers import AccountUserSerializer, InvitationSerializer


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

# # TODO: union queryset with invitations of other suites

# class InvitationView(APIView, TablePagination):
#     permission_classes = (IsAuthenticated,)
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     ordering_fields = ['created_at', 'account', 'account_type', 'invitation_status']
#     ordering = ['-created_at']

#     def get(self, request, format=None):
#         user = self.request.query_params.get('user', None)
#         invitation = Invitation.objects.filter(user=user).exclude(invitation_status='Cancelled')
#         results = self.paginate_queryset(invitation, request, view=self)
#         serializer = InvitationSerializer(results, many=True)
#         return self.get_paginated_response(serializer.data)

# class InvitationDetailView(APIView):
#     permission_classes = (IsAuthenticated,)
    
#     def put(self, request, id, format=None):
#         invitation = Invitation.objects.get(id=id)
#         serializer = InvitationSerializer(invitation, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

# # -----------------------------------------------------------------------------------------------
# # all user suite accounts

# # all accounts of an account belonging to a user
# class AllUserSuiteAccountView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def get(self, request, format=None):
#         personal_id = self.request.query_params.get('personal_id', None)

#         # restaurant accounts
#         restaurant_user = AccountUser.objects.filter(personal_user__id=personal_id)
#         restaurant_serializer = AccountUserSerializer(restaurant_user, many=True)
#         # # restaurant accounts
#         # school_user = AccountUser.objects.filter(personal_user__id=personal_id)
#         # school_serializer = AccountUserSerializer(school_user, many=True)

#         content = {
#             'restaurant': restaurant_serializer.data
#         }

#         return Response(content)

# class AllUserSuiteAccountDetailView(APIView):
#     permission_classes = (IsAuthenticated,)

#     def delete(self, request, id, format=None):
#         account_type = self.request.query_params.get('account_type', None)

#         if account_type == 'restaurant':
#             restaurant_account_user = AccountUser.objects.get(id=id)
#             restaurant_account_user.delete()
#         # if account_type == 'school':
#         #     school_account_user = AccountUser.objects.get(id=id)
#         #     school_account_user.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)

# # --------------------------------------------------------------------------------------
# # dashboard

# @api_view()
# def all_user_suite_account_count(request):
#     personal_id = request.query_params.get('personal_id', None)

#     restaurant_count = AccountUser.objects.filter(personal_user__id=personal_id).count()
#     # school_count = AccountUser.objects.filter(user__id=user).count()

#     content = {'count': restaurant_count}
#     return Response(content)

# @api_view()
# def user_suite_account_share(request):
#     personal_id = request.query_params.get('personal_id', None)

#     restaurant_count = AccountUser.objects.filter(personal_user__id=personal_id).count()
#     # school_count = AccountUser.objects.filter(personal_user__id=personal_id).count()

#     content = {
#         'restaurant': restaurant_count
#     }
    
#     return Response(content)