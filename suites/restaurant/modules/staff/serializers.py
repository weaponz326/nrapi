from rest_framework import serializers

from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Staff
        fields = [
            'id',
            'created_at',
            'account',
            'first_name',
            'last_name',
            'sex',
            'date_of_birth',
            'photo',
            'nationality',
            'religion',
            'phone',
            'email',
            'address',
            'state',
            'city',
            'post_code',
            'staff_code',
            'department',
            'job',
        ]
