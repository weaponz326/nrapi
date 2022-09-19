from rest_framework import serializers

from .models import ExtendedProfile, Invitation


class ExtendedProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedProfile
        fields = [
            'id',
            'updated_at',
            'date_of_birth',
            'gender',
            'country',
            'state',
            'city',
            'phone',
            'address',
        ]

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = [
            'id',
            'created_at',
            'updated_at',
            'user',
            'invitation_status',
            'inviter_type',
            'inviter_invitation_id',
            'inviter_id',
            'inviter_name',
            'inviter_location',
        ]