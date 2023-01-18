from rest_framework import serializers

from .models import Checkin, CheckinCodeConfig


class CheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkin
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CheckinSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class CheckinCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckinCodeConfig
        fields = '__all__'            