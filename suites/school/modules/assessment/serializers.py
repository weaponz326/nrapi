from rest_framework import serializers

from .models import Assessment, AssessmentSheet, AssessmentCodeConfig

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AssessmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class AssessmentSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentSheet
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(AssessmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class AssessmentCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentCodeConfig
        fields = '__all__'