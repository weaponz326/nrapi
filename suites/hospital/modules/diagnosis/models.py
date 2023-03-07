from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hospital.accounts.models import Account
from suites.hospital.modules.admissions.models import Admission


# Create your models here.

class Diagnosis(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    admission = models.ForeignKey(Admission, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    diagnosis_code = models.CharField(max_length=64, null=True, blank=True)
    diagnosis_date = models.DateTimeField(null=True, blank=True)
    consultant_name = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_diagnosis'
        
    def __str__(self):
        return str(self.id)

class DiagnosisReport(CustomBaseModel):
    blood_group = models.CharField(max_length=64, null=True, blank=True)
    temperature = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    blood_presssure = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    pulse = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_diagnosis_report'
        
    def __str__(self):
        return str(self.id)

class DiagnosisCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hospital_module_diagnosis_code_config'

    def __str__(self):
        return str(self.id)
