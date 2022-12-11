from django.db import models

from suites.personal.users.models import CustomBaseModel, User
from suites.enterprise.accounts.models import Account


# Create your models here.

class AccountUser(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    personal_user = models.ForeignKey(User, to_field='id', related_name='enterprise_account_user', on_delete=models.DO_NOTHING)
    is_creator = models.BooleanField(default=False)
    access_level = models.CharField(null=True, max_length=32)

    class Meta:
        db_table = 'enterprise_module_admin_account_user'

    def __str__(self):
        return str(self.id)

class Access(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    admin_access = models.BooleanField(default=False)
    portal_access = models.BooleanField(default=False)
    settings_access = models.BooleanField(default=False)
    accounts_access = models.BooleanField(default=False)
    appraisal_access = models.BooleanField(default=False)
    assets_access = models.BooleanField(default=False)
    attendance_access = models.BooleanField(default=False)
    budget_access = models.BooleanField(default=False)
    employees_access = models.BooleanField(default=False)
    files_access = models.BooleanField(default=False)
    leave_access = models.BooleanField(default=False)
    fiscal_year_access = models.BooleanField(default=False)
    ledger_access = models.BooleanField(default=False)
    letters_access = models.BooleanField(default=False)
    payroll_access = models.BooleanField(default=False)
    procurement_access = models.BooleanField(default=False)
    reception_access = models.BooleanField(default=False)

    class Meta:
        db_table = 'enterprise_module_admin_access'

    def __str__(self):
        return str(self.id)

class Invitation(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, to_field='id', related_name='enterprise_invitee', on_delete=models.DO_NOTHING)
    account_type = models.CharField(null=True, max_length=64)
    invitation_status = models.CharField(null=True, max_length=64)
    date_confirmed = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_admin_invitation'

    def __str__(self):
        return str(self.id)
