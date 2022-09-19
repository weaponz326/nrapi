from rest_framework import serializers

from .models import Rink
from users.serializers import UserSerializer


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
    sender = UserSerializer()
    recipient = UserSerializer()

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
