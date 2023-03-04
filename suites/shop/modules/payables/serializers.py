from rest_framework import serializers

from .models import Payable, PayableCodeConfig


class PayableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payable
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(PayableSerializer, self).__init__(*args, **kwargs)
            request = self.context.get('request')
            if request and (request.method == 'POST' or request.method == 'PUT'):
                self.Meta.depth = 0
            else:
                self.Meta.depth = 1
                
class PayableCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayableCodeConfig
        fields = '__all__'