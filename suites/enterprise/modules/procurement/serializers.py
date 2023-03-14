from rest_framework import serializers

from .models import OrderReview, Procurement, ProcurementCodeConfig


class ProcurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procurement
        fields = '__all__'

class OrderReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderReview
        fields = '__all__'


class ProcurementCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcurementCodeConfig
        fields = '__all__'