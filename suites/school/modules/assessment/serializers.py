from rest_framework import serializers

from .models import Assessment, AssessmentSheet, AssessmentClass, AssessmentCodeConfig

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class AssessmentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentClass
        fields = '__all__'

class AssessmentSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentSheet
        fields = '__all__'

class AssessmentCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentCodeConfig
        fields = '__all__'