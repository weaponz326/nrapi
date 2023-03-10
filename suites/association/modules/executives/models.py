from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.association.accounts.models import Account
from suites.association.modules.members.models import Member


# Create your models here.

class Executive(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    member = models.ForeignKey(Member, to_field='id', on_delete=models.DO_NOTHING)
    # fiscal_year = models.ForeignKey(FiscalYear, to_field='id', on_delete=models.DO_NOTHING)
    position = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'association_module_executive'

    def __str__(self):
        return str(self.id)

class ExecutiveCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'association_module_executive_code_config'

    def __str__(self):
        return str(self.id)
