from rest_framework import serializers

from .models import Dispense, DispenseCodeConfig, DispenseItem


class DispenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispense
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DispenseSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class DispenseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispenseItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DispenseItemSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
            
class DispenseCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispenseCodeConfig
        fields = '__all__'