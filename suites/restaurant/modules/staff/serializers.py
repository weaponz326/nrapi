from rest_framework import serializers

from .models import Staff, StaffCodeConfig


class StaffSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Staff
        fields = '__all__'

class StaffCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffCodeConfig
        fields = '__all__'