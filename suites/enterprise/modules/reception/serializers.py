from rest_framework import serializers

from .models import VisitCodeConfig, Visit


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'

class VisitCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitCodeConfig
        fields = '__all__'