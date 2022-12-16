from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.association.accounts.models import Account


# Create your models here.

class FiscalYear(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    year_code = models.CharField(max_length=32, null=True, blank=True)
    year_name = models.CharField(max_length=256, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    year_status = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        db_table = 'association_module_fiscal_year'

    def __str__(self):
        return str(self.id)

class ActiveFiscalYear(CustomBaseModel):
    year = models.ForeignKey(FiscalYear, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        db_table = 'association_module_active_year'

    def __str__(self):
        return str(self.id)

class FiscalYearCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'association_module_fiscal_year_code_config'

    def __str__(self):
        return str(self.id)
