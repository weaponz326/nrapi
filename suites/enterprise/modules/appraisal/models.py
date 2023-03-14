from django.db import models
from suites.enterprise.modules.employees.models import Employee

from suites.personal.users.models import CustomBaseModel
from suites.enterprise.accounts.models import Account


# Create your models here.

class Appraisal(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    appraisal_code = models.CharField(max_length=64, null=True, blank=True)
    appraisal_name = models.CharField(max_length=256, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    suoervisor = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_appraisal'

    def __str__(self):
        return str(self.id)

class AppraisalSheet(CustomBaseModel):
    knowledge = models.CharField(max_length=4, null=True, blank=True)
    quality = models.CharField(max_length=4, null=True, blank=True)
    productivity = models.CharField(max_length=4, null=True, blank=True)
    dependability = models.CharField(max_length=4, null=True, blank=True)
    attendance = models.CharField(max_length=4, null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_appraisal_sheet'

    def __str__(self):
        return str(self.id)

class AppraisalCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'enterprise_module_appraisal_code_config'

    def __str__(self):
        return str(self.id)
