from rest_framework import serializers

from .models import Customer, CustomerCodeConfig


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

class CustomerCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCodeConfig
        fields = '__all__'