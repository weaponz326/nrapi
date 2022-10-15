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

    def __init__(self, *args, **kwargs):
        super(SectionStudentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class SectionCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionCodeConfig
        fields = '__all__'