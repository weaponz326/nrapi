from rest_framework import serializers

from .models import Reservation, ReservationTable
from modules.customers.serializers import CustomerSerializer
from modules.tables.serializers import TableSerializer


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReservationSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class ReservationTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationTable
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ReservationTableSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1