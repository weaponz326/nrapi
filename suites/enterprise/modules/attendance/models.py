from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.enterprise.accounts.models import Account


# Create your models here.

class Attendance(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    attendance_code = models.CharField(max_length=32, null=True, blank=True)
    attendance_name = models.CharField(max_length=256, null=True, blank=True)
    attendance_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_attendance'

    def __str__(self):
        return str(self.id)

class AttendanceSheet(CustomBaseModel):
    attendance = models.ForeignKey(Attendance, to_field='id', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'enterprise_module_attendance_sheet'

    def __str__(self):
        return str(self.id)

class AttendanceCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'enterprise_module_attendance_code_config'

    def __str__(self):
        return str(self.id)
