from django.db import models

from suites.personal.users.models import CustomBaseModel, User


# Create your models here.

class Budget(CustomBaseModel):
    user = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING)
    budget_name = models.CharField(max_length=128, null=True, blank=True)
    budget_type = models.CharField(max_length=32, null=True)

    class Meta:
        db_table = 'personal_module_budget'

    def __str__(self):
        return str(self.id)

class Income(CustomBaseModel):
    budget = models.ForeignKey(Budget, to_field='id', on_delete=models.DO_NOTHING)
    item_number = models.CharField(max_length=16, null=True, blank=True)
    item_description = models.CharField(max_length=256, null=True, blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    class Meta:
        db_table = 'personal_module_budget_income'

    def __str__(self):
        return str(self.id)

class Expenditure(CustomBaseModel):
    budget = models.ForeignKey(Budget, to_field='id', on_delete=models.DO_NOTHING)
    item_number = models.CharField(max_length=16, null=True, blank=True)
    item_description = models.CharField(max_length=256, null=True, blank=True)
    amount = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    class Meta:
        db_table = 'personal_module_budget_expendture'

    def __str__(self):
        return str(self.id)
