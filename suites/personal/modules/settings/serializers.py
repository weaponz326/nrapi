from rest_framework import serializers

from .models import ExtendedProfile, Invitation


class ExtendedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedProfile
        fields = '__all__'

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = '__all__'
        