from rest_framework import serializers

from .models import ActiveTerm, Term, TermCodeConfig

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'

class ActiveTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveTerm
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ActiveTermSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class TermCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermCodeConfig
        fields = '__all__'