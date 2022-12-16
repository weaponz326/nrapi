from rest_framework import serializers

from .models import AttendanceCodeConfig, Attendance, AttendanceSheet

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class AttendanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceSheet
        fields = '__all__'

class AttendanceCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceCodeConfig
        fields = '__all__'