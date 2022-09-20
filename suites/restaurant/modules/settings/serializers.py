from rest_framework import serializers

from .models import ExtendedProfile, Subscription


class ExtendedProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtendedProfile
        fields = [
            'id',
            'created_at',
            'country',
            'state',
            'city',
            'email',
            'phone',
            'address',
        ]

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = [
            'id',
            'created_at',
            'subscription_type',
            'billing_frequency',
            'number_users',
            'email',
        ]
