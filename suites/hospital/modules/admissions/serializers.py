from rest_framework import serializers

from .models import Admission, AdmissionCodeConfig


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AdmissionSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class AdmissionCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionCodeConfig
        fields = '__all__'