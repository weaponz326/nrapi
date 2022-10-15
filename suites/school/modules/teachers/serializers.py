from rest_framework import serializers

from .models import Teacher, TeacherCodeConfig


class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherCodeConfig
        fields = '__all__'