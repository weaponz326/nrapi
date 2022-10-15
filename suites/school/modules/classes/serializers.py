from rest_framework import serializers

from .models import Clase, ClassStudent, Department

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'

class ClassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassStudent
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'