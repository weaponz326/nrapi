from rest_framework import serializers

from .models import Fees, FeesCodeConfig, FeesTarget

class FeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fees
        fields = '__all__'

class FeesTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesTarget
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FeesTargetSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class FeesCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesCodeConfig
        fields = '__all__'