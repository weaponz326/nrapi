from rest_framework import serializers

from .models import Appointment, AppointmentCodeConfig


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AppointmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class AppointmentCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentCodeConfig
        fields = '__all__'