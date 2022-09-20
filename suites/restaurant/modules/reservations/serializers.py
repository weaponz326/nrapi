from rest_framework import serializers

from .models import Reservation, ReservationTable
from modules.customers.serializers import CustomerSerializer
from modules.tables.serializers import TableSerializer


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'id',
            'created_at',
            'account',
            'customer',
            'customer_name',
            'reservation_code',
            'reservation_date',
            'number_guests',
            'number_tables',
            'arrival_date',
            'reservation_status',
        ]

class ReservationDepthSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Reservation
        fields = [
            'id',
            'created_at',
            'account',
            'customer',
            'customer_name',
            'reservation_code',
            'reservation_date',
            'number_guests',
            'number_tables',
            'arrival_date',
            'reservation_status',
        ]

class ReservationTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationTable
        fields = [
            'id',
            'created_at',
            'reservation',
            'table',
        ]

class ReservationTableDepthSerializer(serializers.ModelSerializer):
    table = TableSerializer()

    class Meta:
        model = ReservationTable
        fields = [
            'id',
            'created_at',
            'reservation',
            'table',
        ]
   