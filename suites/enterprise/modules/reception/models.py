from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.enterprise.accounts.models import Account


# Create your models here.

class Visit(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    visit_code = models.CharField(max_length=64, null=True, blank=True)
    visit_date = models.DateField(null=True, blank=True)
    visitor_name = models.CharField(max_length=256, null=True, blank=True)
    visitor_phone = models.CharField(max_length=256, null=True, blank=True)
    arrival = models.TimeField(null=True, blank=True)
    departure = models.TimeField(null=True, blank=True)
    purpose = models.CharField(max_length=128, null=True, blank=True)
    tag_number = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        db_table = 'enterprise_module_reception_visitor'

    def __str__(self):
        return str(self.id)

class VisitCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'enterprise_module_visit_code_config'

    def __str__(self):
        return str(self.id)