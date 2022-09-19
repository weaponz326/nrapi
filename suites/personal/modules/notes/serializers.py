
from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = [
            'id',
            'updated_at',
            'created_at',
            'user',
            'title',
            'body',
        ]
