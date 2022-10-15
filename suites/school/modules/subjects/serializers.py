from rest_framework import serializers

from .models import Subject, SubjectTeacher, SubjectCodeConfig

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class SubjectTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectTeacher
        fields = '__all__'

class SubjectCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectCodeConfig
        fields = '__all__'