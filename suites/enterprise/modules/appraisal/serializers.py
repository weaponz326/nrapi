from rest_framework import serializers

from .models import Appraisal, AppraisalSheet


class AppraisalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appraisal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AppraisalSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class AppraisalSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppraisalSheet
        fields = '__all__'
