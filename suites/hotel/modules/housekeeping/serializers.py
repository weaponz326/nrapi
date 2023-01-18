from rest_framework import serializers

from .models import Housekeeping, HousekeepingCodeConfig, Checklist


class HousekeepingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Housekeeping
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(HousekeepingSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class ChecklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checklist
        fields = '__all__'

class HousekeepingCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousekeepingCodeConfig
        fields = '__all__'            