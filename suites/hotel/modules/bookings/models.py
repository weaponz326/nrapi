from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.hotel.accounts.models import Account


# Create your models here.

class Booking(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    # guest = models.ForeignKey(Guest, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    booking_code = models.CharField(max_length=64, blank=True)
    booking_date = models.DateTimeField(null=True, blank=True)
    expected_arrival = models.DateTimeField(null=True, blank=True)
    booking_status = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        db_table = 'hotel_module_booking'

    def __str__(self):
        return str(self.id)

class BookedRoom(CustomBaseModel):
    booking = models.ForeignKey(Booking, to_field='id', on_delete=models.DO_NOTHING)
    # room = models.ForeignKey(Room, to_field='id', on_delete=models.DO_NOTHING)
    persons_number = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'hotel_module_booked_room'

    def __str__(self):
        return str(self.id)

class BookingCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'hotel_module_booking_code_config'

    def __str__(self):
        return str(self.id)
