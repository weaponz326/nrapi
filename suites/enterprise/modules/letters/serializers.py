from rest_framework import serializers

from .models import ReceivedLetter, SentLetter


class SentLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentLetter
        fields = '__all__'

class ReceivedLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedLetter
        fields = '__all__'
