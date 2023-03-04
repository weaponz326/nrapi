from rest_framework import serializers

from .models import Prescription, PrescriptionCodeConfig, PrescriptionItem


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PrescriptionSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class PrescriptionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PrescriptionItemSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
            
class PrescriptionCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionCodeConfig
        fields = '__all__'