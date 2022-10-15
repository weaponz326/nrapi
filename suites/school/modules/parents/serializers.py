from rest_framework import serializers

from .models import Parent, ParentWard, ParentCodeConfig

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class ParentWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentWard
        fields = '__all__'

class ParentCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentCodeConfig
        fields = '__all__'