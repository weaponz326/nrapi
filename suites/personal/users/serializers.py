from rest_framework import serializers

from .models import CustomBaseModel, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'created_at',
            'updated_at',
            'email',
            'first_name',
            'last_name',
            'location',
            'about',
            'photo'
        ]
