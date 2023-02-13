from rest_framework import serializers

from .models import Ward, WardPatient, WardCodeConfig

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'

class WardPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardPatient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WardPatientSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class WardCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardCodeConfig
        fields = '__all__'