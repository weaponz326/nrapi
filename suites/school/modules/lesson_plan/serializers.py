from rest_framework import serializers

from .models import LessonPlan, LessonPlanCodeConfig

class LessonPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonPlan
        fields = '__all__'

class LessonPlanCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonPlanCodeConfig
        fields = '__all__'