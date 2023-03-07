
from rest_framework import serializers

from .models import Note, NoteCodeConfig


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = '__all__'

class NoteCodeConfigSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NoteCodeConfig
        fields = '__all__'
