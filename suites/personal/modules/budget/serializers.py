from rest_framework import serializers

from .models import Budget, Income, Expenditure


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = [
            'id',
            'created_at',
            'updated_at',
            'user',
            'budget_name',
            'budget_type',
        ]

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = [
            'id',
            'updated_at',
            'budget',
            'item_number',
            'item_description',
            'amount',
        ]

class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = [
            'id',
            'updated_at',
            'budget',
            'item_number',
            'item_description',
            'amount',
        ]
