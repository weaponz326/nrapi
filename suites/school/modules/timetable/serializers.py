from rest_framework import serializers

from .models import Timetable, TimetableClass, TimetableCodeConfig, TimetablePeriod, TimetableSheet

class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = '__all__'

class TimetableClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimetableClass
        fields = '__all__'

class TimetablePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimetablePeriod
        fields = '__all__'

class TimetableSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimetableSheet
        fields = '__all__'

class TimetableCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimetableCodeConfig
        fields = '__all__'