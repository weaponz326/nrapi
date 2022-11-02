from rest_framework import serializers

from .models import Student, StudentCodeConfig


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class StudentCodeConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCodeConfig
        fields = '__all__'