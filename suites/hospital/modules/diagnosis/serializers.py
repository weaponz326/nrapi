from rest_framework import serializers

from .models import Diagnosis, DiagnosisCodeConfig, DiagnosisReport


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DiagnosisSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class DiagnosisReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisReport
        fields = '__all__'

class DiagnosisCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisCodeConfig
        fields = '__all__'