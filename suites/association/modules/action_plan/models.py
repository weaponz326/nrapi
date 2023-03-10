from pydoc import describe
from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.association.accounts.models import Account


# Create your models here.

class ActionPlan(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    plan_code = models.CharField(max_length=32, null=True, blank=True)
    plan_title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    plan_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'association_module_action_plan'

    def __str__(self):
        return str(self.id)

class PlanStep(CustomBaseModel):
    action_plan = models.ForeignKey(ActionPlan, to_field='id', on_delete=models.DO_NOTHING)
    step_number = models.CharField(max_length=16, null=True, blank=True)
    step_description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'association_module_action_plan_step'

    def __str__(self):
        return str(self.id)

class ActionPlanCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'association_module_action_plan_code_config'

    def __str__(self):
        return str(self.id)
