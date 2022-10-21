from rest_framework import serializers

from .models import Clase, ClassStudent, Department, DepartmentClass

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClassSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class ClassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassStudent
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClassStudentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(DepartmentSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class DepartmentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentClass
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(DepartmentClassSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1