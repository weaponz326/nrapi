from rest_framework import serializers

from .models import Payment, PaymentCodeConfig

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCodeConfig
        fields = '__all__'