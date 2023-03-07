from rest_framework import serializers

from .models import Budget, BudgetCodeConfig, Income, Expenditure


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
        
class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = '__all__'        

class BudgetCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetCodeConfig
        fields = '__all__'
