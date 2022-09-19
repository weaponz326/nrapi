from rest_framework import serializers

from .models import TaskGroup, TaskItem


class TaskGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskGroup
        fields = '__all__'

class TaskItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = TaskItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TaskItemSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1