from rest_framework import serializers

from .models import Student, StudentCodeConfig


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'

class StudentCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCodeConfig
        fields = '__all__'