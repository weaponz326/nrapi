from rest_framework import serializers

from .models import ActiveFiscalYear, FiscalYear, FiscalYearCodeConfig

class FiscalYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalYear
        fields = '__all__'

class ActiveFiscalYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveFiscalYear
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ActiveFiscalYearSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class FiscalYearCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = FiscalYearCodeConfig
        fields = '__all__'