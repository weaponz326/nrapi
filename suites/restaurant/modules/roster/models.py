from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.restaurant.accounts.models import Account
from suites.restaurant.modules.staff.models import Staff


# Create your models here.

class Roster(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    roster_code = models.CharField(max_length=32, blank=True)
    roster_name = models.CharField(max_length=256, blank=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)

    class Meta:
        db_table = 'restaurant_module_roster'

    def __str__(self):
        return str(self.id)

class Shift(CustomBaseModel):
    roster = models.ForeignKey(Roster, to_field='id', on_delete=models.DO_NOTHING)
    shift_name = models.CharField(max_length=256, blank=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    class Meta:
        db_table = 'restaurant_module_roster_shift'

    def __str__(self):
        return str(self.id)

class Batch(CustomBaseModel):
    roster = models.ForeignKey(Roster, to_field='id', on_delete=models.DO_NOTHING)
    batch_name = models.CharField(max_length=256, blank=True)
    batch_symbol = models.CharField(max_length=64, blank=True)

    class Meta:
        db_table = 'restaurant_module_roster_batch'

    def __str__(self):
        return str(self.id)

class StaffPersonnel(CustomBaseModel):
    roster = models.ForeignKey(Roster, to_field='id', on_delete=models.DO_NOTHING)
    staff = models.ForeignKey(Staff, to_field='id', null=True, on_delete=models.DO_NOTHING)
    batch = models.ForeignKey(Batch, to_field='id', null=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'restaurant_module_roster_staff'
        
    def __str__(self):
        return str(self.id)

class RosterDay(CustomBaseModel):
    roster = models.ForeignKey(Roster, to_field='id', on_delete=models.DO_NOTHING)
    shift = models.ForeignKey(Shift, to_field='id', null=True, on_delete=models.DO_NOTHING)
    batch = models.ForeignKey(Batch, to_field='id', null=True, on_delete=models.DO_NOTHING)
    day = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'restaurant_module_roster_day'
        
    def __str__(self):
        return str(self.id)
