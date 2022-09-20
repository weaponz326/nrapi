from rest_framework import serializers

from .models import Rink
from accounts.serializers import AccountSerializer


class RinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rink
        fields = [
            'id',
            'created_at',
            'sender',
            'recipient',
            'rink_type',
            'rink_source',
            'comment',
        ]

class RinkNestedSerializer(serializers.ModelSerializer):
    sender = AccountSerializer()
    recipient = AccountSerializer()

    class Meta:
        model = Rink
        fields = [
            'id',
            'created_at',
            'sender',
            'recipient',
            'rink_type',
            'rink_source',
            'comment',
        ]
