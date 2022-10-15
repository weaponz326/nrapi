from rest_framework import serializers

from .models import Report, ReportAssessment, ReportCodeConfig, ReportSheet

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReportSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class ReportAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportAssessment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReportAssessmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class ReportSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportSheet
        fields = '__all__'

class ReportCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCodeConfig
        fields = '__all__'