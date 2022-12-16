from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.school.accounts.models import Account


# Create your models here.

class Term(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    term_code = models.CharField(max_length=32, null=True, blank=True)
    term_name = models.CharField(max_length=256, null=True, blank=True)
    academic_year = models.CharField(max_length=32, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    term_status = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        db_table = 'school_module_term'

    def __str__(self):
        return str(self.id)

class ActiveTerm(CustomBaseModel):
    term = models.ForeignKey(Term, to_field='id', on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        db_table = 'school_module_active_term'

    def __str__(self):
        return str(self.id)

class TermCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'school_module_term_code_config'

    def __str__(self):
        return str(self.id)
