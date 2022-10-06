from rest_framework import serializers

from .models import StockItem, StockItemCodeConfig


class StockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockItem
        fields = '__all__'

class StockItemCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockItemCodeConfig
        fields = '__all__'