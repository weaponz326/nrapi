from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.association.accounts.models import Account
from suites.association.modules.members.models import Member


# Create your models here.

class Committee(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    committee_chairman = models.ForeignKey(Member, null=True, blank=True, to_field='id', on_delete=models.DO_NOTHING)
    committee_name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date_commissioned = models.DateField(null=True, blank=True)
    date_decommissioned = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'association_module_committee'

    def __str__(self):
        return str(self.id)

class CommitteeMember(CustomBaseModel):
    committee = models.ForeignKey(Committee, to_field='id', on_delete=models.DO_NOTHING)
    member = models.ForeignKey(Member, to_field='id', on_delete=models.DO_NOTHING)
    
    class Meta:
        db_table = 'association_module_committee_member'

    def __str__(self):
        return str(self.id)

class CommitteeCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'association_module_committee_code_config'

    def __str__(self):
        return str(self.id)
