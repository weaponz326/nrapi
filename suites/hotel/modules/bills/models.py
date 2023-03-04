from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hotel.accounts.models import Account


# Create your models here.

class Bill(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    # guest = models.ForeignKey(Guest, to_field='id', on_delete=models.DO_NOTHING)
    bill_code = models.CharField(max_length=64, blank=True)
    bill_date = models.DateTimeField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    class Meta:
        db_table = 'hotel_module_bill'

    def __str__(self):
        return str(self.id)

class CheckinCharge(CustomBaseModel):
    bill = models.ForeignKey(Bill, to_field='id', on_delete=models.DO_NOTHING)
    item_number = models.IntegerField(null=True, blank=True)
    # checkin = models.ForeignKey(Checkin, to_field='id', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'hotel_module_bill_checkin_charge'

    def __str__(self):
        return str(self.id)

class ServiceCharge(CustomBaseModel):
    # service = models.ForeignKey(Service, to_field='id', on_delete=models.DO_NOTHING)
    item_number = models.IntegerField(null=True, blank=True)
    bill = models.ForeignKey(Bill, to_field='id', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'hotel_module_bill_service_charge'

    def __str__(self):
        return str(self.id)

class BillCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hotel_module_bill_code_config'

    def __str__(self):
        return str(self.id)
