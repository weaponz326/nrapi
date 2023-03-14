from django.contrib import admin

from .models import Budget, BudgetCodeConfig, Income, Expenditure


# Register your models here.

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('pkid','id', 'created_at', 'account', 'budget_name', 'budget_type')

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('pkid','id', 'created_at', 'budget', 'item_number', 'amount')

class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('pkid','id', 'created_at', 'budget', 'item_number', 'amount')

class BudgetCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Budget, BudgetAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expenditure, ExpenditureAdmin)
admin.site.register(BudgetCodeConfig, BudgetCodeConfigAdmin)
