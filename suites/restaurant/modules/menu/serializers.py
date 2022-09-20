from rest_framework import serializers

from .models import MenuGroup, MenuItem


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
