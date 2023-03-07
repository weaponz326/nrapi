from django.contrib import admin
from .models import TaskGroup, TaskGroupCodeConfig, TaskItem, TaskItemCodeConfig


# Register your models here.

class TaskGroupAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'user', 'task_group', 'created_at')

class TaskItemAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'updated_at', 'task_group', 'task_item', 'priority', 'status')

class TaskGroupCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

class TaskItemCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(TaskGroup, TaskGroupAdmin)
admin.site.register(TaskItem, TaskItemAdmin)
admin.site.register(TaskGroupCodeConfig, TaskGroupCodeConfigAdmin)
admin.site.register(TaskItemCodeConfig, TaskItemCodeConfigAdmin)
