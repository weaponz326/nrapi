from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.restaurant.accounts.models import Account


# Create your models here.

class Table(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    table_number = models.CharField(max_length=64, null=True, blank=True)
    table_type = models.CharField(max_length=128, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    table_status = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'restaurant_module_table'
        
    def __str__(self):
        return str(self.id)
