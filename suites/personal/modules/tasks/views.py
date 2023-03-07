import datetime
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.db.models.functions import TruncDate
from django.dispatch import receiver
from django.db.models.signals import post_save

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view

from suites.personal.users.models import User

from .models import TaskGroup, TaskGroupCodeConfig, TaskItem, TaskItemCodeConfig
from .serializers import TaskGroupCodeConfigSerializer, TaskGroupSerializer, TaskItemCodeConfigSerializer, TaskItemSerializer
from suites.personal.users.paginations import TablePagination
from suites.personal.users.services import fiil_zero_dates, generate_code, get_initials


# Create your views here.

class TaskGroupView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['task_group', 'created_at']
    ordering = ['-created_at']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        task_group = TaskGroup.objects.filter(user=user).order_by('-created_at')
        results = self.paginate_queryset(task_group, request, view=self)
        serializer = TaskGroupSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TaskGroupDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        task_group = TaskGroup.objects.get(id=id)
        serializer = TaskGroupSerializer(task_group)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        task_group = TaskGroup.objects.get(id=id)
        serializer = TaskGroupSerializer(task_group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        task_group = TaskGroup.objects.get(id=id)
        task_group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------------------
# task item

class AllTaskItemView(APIView, TablePagination):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['created_at', 'task_group', 'task_item', 'priority', 'start_date', 'end_date', 'status']
    ordering = ['-created_at']

    def get(self, request, format=None):
        user = self.request.query_params.get('user', None)
        task_item = TaskItem.objects.filter(task_group__user=user).order_by('-created_at')
        results = self.paginate_queryset(task_item, request, view=self)
        serializer = TaskItemSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)

class TaskItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        task_group = self.request.query_params.get('task_group', None)
        task_item = TaskItem.objects.filter(task_group=task_group).order_by('-created_at')
        serializer = TaskItemSerializer(task_item, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TaskItemDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        task_item = TaskItem.objects.get(id=id)
        serializer = TaskItemSerializer(task_item)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        task_item = TaskItem.objects.get(id=id)
        serializer = TaskItemSerializer(task_item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id, format=None):
        task_item = TaskItem.objects.get(id=id)
        task_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --------------------------------------------------------------------------------------
# config

# task group

class TaskGroupCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = TaskGroupCodeConfig.objects.get(id=id)
        serializer = TaskGroupCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = TaskGroupCodeConfig.objects.get(id=id)
        serializer = TaskGroupCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewTaskGroupCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = TaskGroupCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = TaskGroupCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=User)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        TaskGroupCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.first_name) + ' ' + get_initials(instance.last_name),
            suffix="CA",
            last_code="0000"
        )

# schedule

class TaskItemCodeConfigDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code = TaskItemCodeConfig.objects.get(id=id)
        serializer = TaskItemCodeConfigSerializer(code)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        code = TaskItemCodeConfig.objects.get(id=id)
        serializer = TaskItemCodeConfigSerializer(code, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class NewTaskItemCodeConfigView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id, format=None):
        code_set = TaskItemCodeConfig.objects.get(id=id)
        new_code = generate_code(code_set.last_code)                

        if code_set.entry_mode == 'Auto':
            code = TaskItemCodeConfig.objects.filter(id=id)
            code.update(last_code=new_code)
            content = {'code': '{}{}{}'.format(code_set.prefix, new_code, code_set.suffix)}
            return Response(content)
        return Response(status.HTTP_204_NO_CONTENT)

@receiver(post_save, sender=User)
def save_extended_profile(sender, instance, created, **kwargs):
    if created:
        TaskItemCodeConfig.objects.create(
            id=instance.id,
            entry_mode="Auto",
            prefix=get_initials(instance.first_name) + ' ' + get_initials(instance.last_name),
            suffix="SD",
            last_code="000000"
        )

# --------------------------------------------------------------------------------------
# dashboard

@api_view()
def task_group_count(request):
    count = TaskGroup.objects\
        .filter(user__id=request.query_params.get('user', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def task_item_count(request):
    count = TaskItem.objects\
        .filter(task_group__user__id=request.query_params.get('user', None))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def all_todo_count(request):
    count = TaskItem.objects\
        .filter(task_group__user__id=request.query_params.get('user', None), status="To Do")\
        .count()           
    content = {'count': count}
    return Response(content)

@api_view()
def task_group_annotate(request):
    items = TaskGroup.objects\
        .filter(user__id=request.query_params.get('user', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_items = fiil_zero_dates(items)
    return Response(filled_items)

@api_view()
def task_item_annotate(request):
    items = TaskItem.objects\
        .filter(task_group__user__id=request.query_params.get('user', None))\
        .annotate(date=TruncDate('created_at'))\
        .filter(created_at__lte=datetime.datetime.today(), created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30))\
        .values('date').annotate(count=Count('id')).order_by('-date')
    filled_items = fiil_zero_dates(items)
    return Response(filled_items)
