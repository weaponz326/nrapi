from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hotel.accounts.models import Account
from suites.hotel.modules.guests.models import Guest


# Create your models here.

class Service(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    guest = models.ForeignKey(Guest, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    service_code = models.CharField(max_length=64, null=True, blank=True)
    service_name = models.CharField(max_length=256, null=True, blank=True)
    service_type = models.CharField(max_length=64, null=True, blank=True)
    service_total = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    class Meta:
        db_table = 'hotel_module_service'

    def __str__(self):
        return str(self.id)

class ServiceItem(CustomBaseModel):
    service = models.ForeignKey(Service, to_field='id', on_delete=models.DO_NOTHING)
    item_number = models.IntegerField(null=True, blank=True)
    item_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    class Meta:
        db_table = 'hotel_module_service_item'

    def __str__(self):
        return str(self.id)

class ServiceCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hotel_module_service_code_config'

    def __str__(self):
        return str(self.id)
