from rest_framework import serializers

from .models import Booking, BookingCodeConfig, BookedRoom


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BookingSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class BookedRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedRoom
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(BookedRoomSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class BookingCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingCodeConfig
        fields = '__all__'            