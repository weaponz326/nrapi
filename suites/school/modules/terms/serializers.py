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

class TermCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermCodeConfig
        fields = '__all__'