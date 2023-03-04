from rest_framework import serializers

from .models import Supplier, SupplierCodeConfig, SupplierItem


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'

class SupplierItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SupplierItemSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
            
class SupplierCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierCodeConfig
        fields = '__all__'