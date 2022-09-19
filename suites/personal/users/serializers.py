from rest_framework import serializers

from .models import CustomBaseModel, User


# # TODO: custom base serializer not working
# class CustomBaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomBaseModel
#         fields = ['id', 'created_at', 'updated_at']

# class UserSerializer(CustomBaseSerializer):
#     class Meta:
#         model = User
#         fields = [
#             'email',
#             'first_name',
#             'last_name',
#             'location',
#             'about',
#             'photo'
#         ]

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
