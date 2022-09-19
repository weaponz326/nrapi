from django.db import models

from users.models import CustomBaseModel, User


# Create your models here.

class TaskGroup(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    task_group = models.CharField(max_length=256, null=True)

    def __str__(self):
        return str(self.id)

class TaskItem(CustomBaseModel):
    task_group = models.ForeignKey(TaskGroup, to_field='id', on_delete=models.CASCADE)
    task_item = models.CharField(max_length=256, null=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    priority = models.CharField(max_length=16, null=True)
    status = models.CharField(max_length=16, null=True)

    def __str__(self):
        return str(self.id)
