from rest_framework import serializers

from .models import Laboratory, LaboratoryCodeConfig


class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LaboratorySerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class LaboratoryCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryCodeConfig
        fields = '__all__'