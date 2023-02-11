from django.db import models

from suites.personal.users.models import CustomBaseModel, User
from suites.hospital.accounts.models import Account


# Create your models here.

class AccountUser(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    personal_user = models.ForeignKey(User, to_field='id', related_name='hospital_account_user', on_delete=models.DO_NOTHING)
    is_creator = models.BooleanField(default=False)
    access_level = models.CharField(null=True, max_length=32)

    class Meta:
        db_table = 'hospital_module_admin_account_user'

    def __str__(self):
        return str(self.id)

class Access(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    admin_access = models.BooleanField(default=False)
    portal_access = models.BooleanField(default=False)
    settings_access = models.BooleanField(default=False)
    patients_access = models.BooleanField(default=False)
    appointments_access = models.BooleanField(default=False)
    staff_access = models.BooleanField(default=False)
    bills_access = models.BooleanField(default=False)
    doctors_access = models.BooleanField(default=False)
    laboratory_access = models.BooleanField(default=False)
    payments_access = models.BooleanField(default=False)
    nurses_access = models.BooleanField(default=False)
    prescriptions_access = models.BooleanField(default=False)
    diagnosis_access = models.BooleanField(default=False)
    drugs_access = models.BooleanField(default=False)
    wards_access = models.BooleanField(default=False)
    admissions_access = models.BooleanField(default=False)
    dispensary_access = models.BooleanField(default=False)
    roster_access = models.BooleanField(default=False)

    class Meta:
        db_table = 'hospital_module_admin_access'

    def __str__(self):
        return str(self.id)

class Invitation(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, to_field='id', related_name='hospital_invitee', on_delete=models.DO_NOTHING)
    account_type = models.CharField(null=True, max_length=64)
    invitation_status = models.CharField(null=True, max_length=64)
    date_confirmed = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'hospital_module_admin_invitation'

    def __str__(self):
        return str(self.id)
