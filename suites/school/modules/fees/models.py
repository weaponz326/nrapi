from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account
from suites.school.modules.classes.models import Clase


# Create your models here.

class Fees(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    fees_code = models.CharField(max_length=32, null=True, blank=True)
    fees_name = models.CharField(max_length=256, null=True, blank=True)
    fees_description = models.TextField(null=True, blank=True)
    fees_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'school_module_fees'

    def __str__(self):
        return str(self.id)

class FeesTarget(CustomBaseModel):
    fees = models.ForeignKey(Fees, to_field='id', on_delete=models.DO_NOTHING)
    clase = models.ForeignKey(Clase, to_field='id', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'school_module_fees_target'

    def __str__(self):
        return str(self.id)

class FeesCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'school_module_fees_code_config'

    def __str__(self):
        return str(self.id)
