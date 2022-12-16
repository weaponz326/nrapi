from django.db import models
from suites.enterprise.modules.employees.models import Employee

from suites.personal.users.models import CustomBaseModel
from suites.enterprise.accounts.models import Account


# Create your models here.

class Leave(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, to_field='id', on_delete=models.DO_NOTHING)
    leave_code = models.CharField(max_length=64, null=True, blank=True)
    leave_type = models.CharField(max_length=256, null=True, blank=True)
    leave_start = models.DateField(null=True, blank=True)
    leave_end = models.DateField(null=True, blank=True)
    leave_status = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_leave'

    def __str__(self):
        return str(self.id)
