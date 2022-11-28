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
