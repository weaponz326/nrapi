from rest_framework import serializers

from .models import Employee, EmployeeCodeConfig


class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class EmployeeCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCodeConfig
        fields = '__all__'