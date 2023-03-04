from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hotel.accounts.models import Account


# Create your models here.

class Checkin(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    # guest = models.ForeignKey(Guest, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    checkin_code = models.CharField(max_length=64, blank=True)
    from_booking = models.BooleanField(null=True, blank=True)
    booking_code = models.CharField(max_length=64, null=True, blank=True)
    checkin_date = models.DateTimeField(null=True, blank=True)
    checkout_date = models.DateTimeField(null=True, blank=True)
    number_nights = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'hotel_module_checkin'

    def __str__(self):
        return str(self.id)

class CheckinCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hotel_module_checkin_code_config'

    def __str__(self):
        return str(self.id)
