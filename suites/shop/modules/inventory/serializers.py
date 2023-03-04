from rest_framework import serializers

from .models import Inventory, InventoryCodeConfig


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InventorySerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class InventoryCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryCodeConfig
        fields = '__all__'