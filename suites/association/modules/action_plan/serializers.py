from rest_framework import serializers

from .models import ActionPlan, PlanStep


class ActionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionPlan
        fields = '__all__'

class PlanStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanStep
        fields = '__all__'
        