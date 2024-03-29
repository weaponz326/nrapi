from rest_framework import serializers

from .models import Bill, BillCodeConfig


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BillSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class BillCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillCodeConfig
        fields = '__all__'