from rest_framework import serializers

from .models import ActionPlan, ActionPlanCodeConfig, PlanStep


class ActionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionPlan
        fields = '__all__'

class PlanStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanStep
        fields = '__all__'
        
class ActionPlanCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionPlanCodeConfig
        fields = '__all__'