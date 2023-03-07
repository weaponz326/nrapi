from rest_framework import serializers

from .models import Calendar, CalendarCodeConfig, Schedule, ScheduleCodeConfig


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ScheduleSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class CalendarCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarCodeConfig
        fields = '__all__'

class ScheduleCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleCodeConfig
        fields = '__all__'