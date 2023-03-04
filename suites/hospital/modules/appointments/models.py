from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hospital.accounts.models import Account
from suites.hospital.modules.patients.models import Patient


# Create your models here.

class Appointment(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    patient = models.ForeignKey(Patient, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)
    appointment_code = models.CharField(max_length=64, null=True, blank=True)
    appointment_date = models.DateTimeField(null=True, blank=True)
    appointment_status = models.CharField(max_length=128, null=True, blank=True)
    consultant_name = models.CharField(max_length=256, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_appointment'
        
    def __str__(self):
        return str(self.id)

class AppointmentCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hospital_module_appointment_code_config'

    def __str__(self):
        return str(self.id)
