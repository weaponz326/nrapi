from rest_framework import serializers

from .models import Parent, ParentWard, ParentCodeConfig

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class ParentWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentWard
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ParentWardSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class ParentCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentCodeConfig
        fields = '__all__'