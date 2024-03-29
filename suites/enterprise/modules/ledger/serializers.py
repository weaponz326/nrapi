from rest_framework import serializers

from .models import Ledger, LedgerItem


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = '__all__'

class LedgerItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LedgerItemSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1