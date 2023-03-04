from rest_framework import serializers

from .models import Drug, DrugCodeConfig


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'

class DrugCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrugCodeConfig
        fields = '__all__'