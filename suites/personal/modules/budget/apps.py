from django.apps import AppConfig


class BudgetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.personal.modules.budget'
    label = 'personal_module_budget'
    verbose_name = 'personal module budget'
