from rest_framework import serializers

from .models import AccountUser, Access, Invitation


class AccountUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AccountUserSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InvitationSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
