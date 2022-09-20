from django.db import models

from accounts.models import CustomBaseModel, Account
from modules.customers.models import Customer
from modules.tables.models import Table


# Create your models here.

class Reservation(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, to_field='id', null=True, blank=True, on_delete=models.DO_NOTHING)
    customer_name = models.CharField(max_length=256, blank=True)
    reservation_code = models.CharField(max_length=64, blank=True)
    reservation_date = models.DateTimeField(null=True, blank=True)
    number_guests = models.IntegerField(null=True, blank=True)
    number_tables = models.IntegerField(null=True, blank=True)
    arrival_date = models.DateTimeField(null=True, blank=True)
    reservation_status = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.id)

class ReservationTable(CustomBaseModel):
    reservation = models.ForeignKey(Reservation, to_field='id', on_delete=models.DO_NOTHING)
    table = models.ForeignKey(Table, to_field='id', on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)
