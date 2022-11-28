from rest_framework import serializers

from .models import Group, GroupMember, GroupCodeConfig

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMember
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(GroupMemberSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class GroupCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCodeConfig
        fields = '__all__'