from rest_framework import serializers

from .models import AttendanceCodeConfig, StudentAttendance, StudentAttendanceSheet, TeacherAttendance, TeacherAttendanceSheet

class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentAttendanceSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

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