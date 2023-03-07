from django.db import models

from suites.personal.users.models import CustomBaseModel, User


# Create your models here.

class Calendar(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING)
    calendar_code = models.CharField(null=True, blank=True, max_length=32)
    calendar_name = models.CharField(null=True, blank=True, max_length=256)

    class Meta:
        db_table = 'personal_module_calendar'

    def __str__(self):
        return str(self.id)

class Schedule(CustomBaseModel):
    calendar = models.ForeignKey(Calendar, to_field='id', on_delete=models.DO_NOTHING)
    schedule_code = models.CharField(null=True, blank=True, max_length=64)
    schedule_name = models.CharField(null=True, blank=True, max_length=256)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(null=True, blank=True, max_length=256)
    status = models.CharField(null=True, blank=True, max_length=32)

    class Meta:
        db_table = 'personal_module_calendar_schedule'

    def __str__(self):
        return str(self.id)

class CalendarCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'personal_module_calendar_code_config'

    def __str__(self):
        return str(self.id)

class ScheduleCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'personal_module_calendar_schedule_code_config'

    def __str__(self):
        return str(self.id)
