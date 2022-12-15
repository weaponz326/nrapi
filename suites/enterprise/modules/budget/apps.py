from django.apps import AppConfig


class BudgetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.enterprise.modules.budget'
    label = 'enterprise_module_budget'
    verbose_name = 'enterprise module budget'
