from rest_framework import serializers

from .models import MenuGroup, MenuGroupCodeConfig, MenuItem, MenuItemCodeConfig


class MenuGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuGroup
        fields = '__all__'


class MenuItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = MenuItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MenuItemSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class MenuGroupCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuGroupCodeConfig
        fields = '__all__'

class MenuItemCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemCodeConfig
        fields = '__all__'
