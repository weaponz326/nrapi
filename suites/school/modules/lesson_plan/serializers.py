from rest_framework import serializers

from .models import LessonPlan, LessonPlanCodeConfig

class LessonPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonPlan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LessonPlanSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class LessonPlanCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonPlanCodeConfig
        fields = '__all__'