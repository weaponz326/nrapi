from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hospital.accounts.models import Account
from suites.hospital.modules.admissions.models import Admission


# Create your models here.

class Laboratory(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    admission = models.ForeignKey(Admission, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    lab_code = models.CharField(max_length=64, null=True, blank=True)
    lab_date = models.DateTimeField(null=True, blank=True)
    lab_type = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_laboratory'
        
    def __str__(self):
        return str(self.id)

class LaboratoryCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hospital_module_laboratory_code_config'

    def __str__(self):
        return str(self.id)
