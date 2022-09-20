from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            'id',
            'created_at',
            'account',
            'customer_code',
            'customer_name',
            'customer_type',
            'phone',
            'email',
            'address',
            'state',
            'city',
            'post_code',
            'allergies',
            'preferences',
        ]
