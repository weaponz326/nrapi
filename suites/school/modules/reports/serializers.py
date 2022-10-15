from rest_framework import serializers

from .models import Report, ReportAssessment, ReportCodeConfig, ReportSheet

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class ReportAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportAssessment
        fields = '__all__'

class ReportSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportSheet
        fields = '__all__'

class ReportCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCodeConfig
        fields = '__all__'