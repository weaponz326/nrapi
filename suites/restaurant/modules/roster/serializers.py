from rest_framework import serializers

from .models import (
    Roster,
    Shift,
    Batch,
    StaffPersonnel,
    RosterDay
)

class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roster
        fields = '__all__'

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class StaffPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPersonnel
        fields = '__all__'

class RosterDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RosterDay
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RosterDaySerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
