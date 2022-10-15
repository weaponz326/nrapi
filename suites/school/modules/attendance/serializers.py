from rest_framework import serializers

from .models import AttendanceCodeConfig, StudentAttendance, StudentAttendanceSheet, TeacherAttendance, TeacherAttendanceSheet

class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'

class StudentAttendanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendanceSheet
        fields = '__all__'

class TeacherAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherAttendance
        fields = '__all__'

class TeacherAttendanceSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherAttendanceSheet
        fields = '__all__'

class AttendanceCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceCodeConfig
        fields = '__all__'