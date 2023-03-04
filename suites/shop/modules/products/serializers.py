from rest_framework import serializers

from .models import Product, ProductCodeConfig


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

class ProductCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCodeConfig
        fields = '__all__'