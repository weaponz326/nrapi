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
        fields = [
            'id',
            'created_at',
            'account',
            'roster_code',
            'roster_name',
            'from_date',
            'to_date',
        ]

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = [
            'id',
            'created_at',
            'roster',
            'shift_name',
            'start_time',
            'end_time',
        ]

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = [
            'id',
            'created_at',
            'roster',
            'batch_name',
            'batch_symbol',
        ]

class StaffPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffPersonnel
        fields = [
            'id',
            'created_at',
            'roster',
            'staff',
            'batch',
        ]

class RosterDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RosterDay
        fields = [
            'id',
            'created_at',
            'roster',
            'day',
        ]

class RosterSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RosterSheet
        fields = [
            'id',
            'created_at',
            'roster_day',
            'shift',
            'batch',
        ]
