from rest_framework import serializers

from .models import Receivable, ReceivableCodeConfig


class ReceivableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receivable
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(ReceivableSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and (request.method == 'POST' or request.method == 'PUT'):
                self.Meta.depth = 0
            else:
                self.Meta.depth = 1
                
class ReceivableCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivableCodeConfig
        fields = '__all__'