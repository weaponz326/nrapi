from rest_framework import serializers

from .models import Patient, PatientCodeConfig


class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PatientSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class PatientCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientCodeConfig
        fields = '__all__'