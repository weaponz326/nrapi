from rest_framework import serializers

from .models import Asset, AssetCodeConfig


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class AssetCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCodeConfig
        fields = '__all__'