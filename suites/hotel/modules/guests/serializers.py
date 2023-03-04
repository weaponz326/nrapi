from rest_framework import serializers

from .models import Guest, GuestCodeConfig


class GuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guest
        fields = '__all__'

class GuestCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestCodeConfig
        fields = '__all__'