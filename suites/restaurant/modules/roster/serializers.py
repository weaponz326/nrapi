from rest_framework import serializers

from .models import (
    Roster,
    RosterSheet,
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

class RosterSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RosterSheet
        fields = '__all__'
