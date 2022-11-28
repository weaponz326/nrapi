from django.contrib import admin

from .models import ActionPlan, PlanStep


# Register your models here.

class ActionPlanAdmin(admin.ModelAdmin):
    list_display = ('pkid','id', 'created_at', 'account', 'plan_code', 'plan_title', 'plan_date')

class PlanStepAdmin(admin.ModelAdmin):
    list_display = ('pkid','id', 'created_at', 'action_plan', 'step_number')

admin.site.register(ActionPlan, ActionPlanAdmin)
admin.site.register(PlanStep, PlanStepAdmin)
