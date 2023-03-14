from django.db import models
from suites.enterprise.modules.employees.models import Employee

from suites.personal.users.models import CustomBaseModel
from suites.enterprise.accounts.models import Account


# Create your models here.

class Leave(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    leave_code = models.CharField(max_length=64, null=True, blank=True)
    leave_type = models.CharField(max_length=256, null=True, blank=True)
    leave_start = models.DateField(null=True, blank=True)
    leave_end = models.DateField(null=True, blank=True)
    leave_status = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_leave'

    def __str__(self):
        return str(self.id)

class LeaveCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'enterprise_module_leave_code_config'

    def __str__(self):
        return str(self.id)