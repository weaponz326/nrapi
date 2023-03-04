from rest_framework import serializers

from .models import Doctor, DoctorCodeConfig


class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Doctor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DoctorSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class DoctorCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorCodeConfig
        fields = '__all__'