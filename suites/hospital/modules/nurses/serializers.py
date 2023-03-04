from rest_framework import serializers

from .models import Nurse, NurseCodeConfig


class NurseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Nurse
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NurseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class NurseCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseCodeConfig
        fields = '__all__'