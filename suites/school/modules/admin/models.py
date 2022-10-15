from django.db import models

from suites.personal.users.models import CustomBaseModel, User
from suites.school.accounts.models import Account


# Create your models here.

class AccountUser(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    personal_user = models.ForeignKey(User, to_field='id', related_name='school_account_user', on_delete=models.DO_NOTHING)
    is_creator = models.BooleanField(default=False)
    access_level = models.CharField(null=True, max_length=32)

    class Meta:
        db_table = 'school_module_admin_account_user'

    def __str__(self):
        return str(self.id)

class Access(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    admin_access = models.BooleanField(default=False)
    portal_access = models.BooleanField(default=False)
    settings_access = models.BooleanField(default=False)
    parents_access = models.BooleanField(default=False)
    assessment_access = models.BooleanField(default=False)
    subjects_access = models.BooleanField(default=False)
    attendance_access = models.BooleanField(default=False)
    students_access = models.BooleanField(default=False)
    lesson_plan_access = models.BooleanField(default=False)
    reports_access = models.BooleanField(default=False)
    teachers_access = models.BooleanField(default=False)
    payments_access = models.BooleanField(default=False)
    classes_access = models.BooleanField(default=False)
    timetable_access = models.BooleanField(default=False)
    fees_access = models.BooleanField(default=False)
    sections_access = models.BooleanField(default=False)
    

    class Meta:
        db_table = 'school_module_admin_access'

    def __str__(self):
        return str(self.id)

class Invitation(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, to_field='id', related_name='school_invitee', on_delete=models.DO_NOTHING)
    account_type = models.CharField(null=True, max_length=64)
    invitation_status = models.CharField(null=True, max_length=64)
    date_confirmed = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'school_module_admin_invitation'

    def __str__(self):
        return str(self.id)
