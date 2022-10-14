import json

from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, status
from rest_framework.permissions import IsAuthenticated

from .models import ExtendedProfile, Subscription, SubscriptionEvent
from .serializers import ExtendedProfileSerializer, SubscriptionEventSerializer, SubscriptionSerializer
from suites.school.accounts.models import Account
import suites.personal.payments.services as PaystackPayments


# Create your views here.

class ExtendedProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        profile = ExtendedProfile.objects.filter(id=account)
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
        rink = ExtendedProfile.objects.get(id=id)
        serializer = ExtendedProfileSerializer(rink)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        rink = ExtendedProfile.objects.get(id=id)
        serializer = ExtendedProfileSerializer(rink, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)        

    def delete(self, request, id, format=None):
        rink = ExtendedProfile.objects.get(id=id)
        rink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------------------------
# subscriptions

class SubscriptionDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        subscription = Subscription.objects.get(id=id)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        subscription = Subscription.objects.filter(id=id)
        serializer = SubscriptionSerializer(subscription, data=request.data, partial=True)
        
        if serializer.is_valid():
            result = PaystackPayments.innitialize_transaction(request.data)
            print(result)

            if result['status'] == True:
                subscription.update(
                    subscription_type = request.data['subscription_type'],
                    billing_frequency = request.data['billing_frequency'],
                    number_users = request.data['number_users'],
                    status = request.data['status'],
                    email = request.data['email'],
                    plan = request.data['plan'],
                    quantity = request.data['quantity'],
                )

                return Response(result)
            return Response({'messsage': 'Payment failed'})
        return Response(serializer.errors)

# ---------------------------------------------------------------------------------------------------
# subscription events

class SubscriptionEventView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        subscription = SubscriptionEvent.objects.filter(account=account).order_by('-created_at')
        serializer = SubscriptionEventSerializer(subscription, many=True)
        return Response(serializer.data)

# ------------------------------------------------------------------------------------------

@receiver(post_save, sender=Account)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        ExtendedProfile.objects.create(
            id=instance.id
        )

@receiver(post_save, sender=Account)
def save_subscription(sender, instance, created, **kwargs):
    if created:

        Subscription.objects.create(
            id=instance.id,
            subscription_type="Individual",
            number_users=1,
            status="Active"
        )
