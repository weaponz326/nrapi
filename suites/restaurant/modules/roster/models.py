from django.db import models

from accounts.models import CustomBaseModel, Account
from modules.staff.models import Staff


# Create your models here.

class Roster(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    roster_code = models.CharField(max_length=32, blank=True)
    roster_name = models.CharField(max_length=256, blank=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)

    def __str__(self):
        return str(self.id)

class Shift(CustomBaseModel):
    roster = models.ForeignKey(Roster, to_field='id', on_delete=models.DO_NOTHING)
    shift_name = models.CharField(max_length=256, blank=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    def __str__(self):
        return str(self.id)

class Batch(CustomBaseModel):
    roster = models.ForeignKey(Roster, to_field='id', on_delete=models.DO_NOTHING)
    batch_name = models.CharField(max_length=256, blank=True)
    batch_symbol = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return str(self.id)

class StaffPersonnel(CustomBaseModel):
    roster = models.ForeignKey(Roster, to_field='id', on_delete=models.DO_NOTHING)
    staff = models.ForeignKey(Staff, to_field='id', null=True, on_delete=models.DO_NOTHING)
    batch = models.ForeignKey(Batch, to_field='id', null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)

# TODO: to be removed
class RosterDay(CustomBaseModel):
    roster = models.ForeignKey(Roster, to_field='id', on_delete=models.DO_NOTHING)
    day = models.DateField(null=True, blank=True)

class RosterSheet(CustomBaseModel):
    roster_day = models.ForeignKey(RosterDay, to_field='id', null=True, on_delete=models.DO_NOTHING)
    shift = models.ForeignKey(Shift, null=True, on_delete=models.DO_NOTHING)
    batch = models.ForeignKey(Batch, null=True, on_delete=models.DO_NOTHING)
    # shift = models.ForeignKey(Shift, null=True, on_delete=models.DO_NOTHING)
    # sheet_days = models.JSONField(null=True, blank=True)
