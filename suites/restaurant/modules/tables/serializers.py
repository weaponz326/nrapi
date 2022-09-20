from rest_framework import serializers

from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = [
            'id',
            'created_at',
            'account',
            'table_number',
            'table_type',
            'capacity',
            'location',
            'table_status',
        ]
