from rest_framework import serializers

from .models import Section, SectionStudent, SectionCodeConfig

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class SectionStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionStudent
        fields = '__all__'

class SectionCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionCodeConfig
        fields = '__all__'