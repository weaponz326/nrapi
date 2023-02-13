from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hospital.accounts.models import Account
from suites.hospital.modules.patients.models import Patient


# Create your models here.

class Ward(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    ward_number = models.CharField(max_length=32, null=True, blank=True)
    ward_name = models.CharField(max_length=256, null=True, blank=True)
    ward_type = models.CharField(max_length=256, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_ward'

    def __str__(self):
        return str(self.id)

class WardPatient(CustomBaseModel):
    ward = models.ForeignKey(Ward, to_field='id', on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, to_field='id', on_delete=models.DO_NOTHING)
    checkin_date = models.DateField(null=True, blank=True)
    checkout_date = models.DateField(null=True, blank=True)
    bed_number = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_ward_patient'

    def __str__(self):
        return str(self.id)

class WardCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hospital_module_ward_code_config'

    def __str__(self):
        return str(self.id)
