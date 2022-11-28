from rest_framework import serializers

from .models import Member, MemberCodeConfig


class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Member
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MemberSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class MemberCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberCodeConfig
        fields = '__all__'