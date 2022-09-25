from django.db import models

from suites.personal.users.models import CustomBaseModel, User


# Create your models here.

class TaskGroup(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING)
    task_group = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'personal_module_task_group'

    def __str__(self):
        return str(self.id)

class TaskItem(CustomBaseModel):
    task_group = models.ForeignKey(TaskGroup, to_field='id', on_delete=models.DO_NOTHING)
    task_item = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    priority = models.CharField(max_length=32, null=True)
    status = models.CharField(max_length=32, null=True)

    class Meta:
        db_table = 'personal_module_task_item'

    def __str__(self):
        return str(self.id)
