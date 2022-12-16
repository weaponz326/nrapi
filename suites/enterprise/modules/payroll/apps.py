from django.apps import AppConfig


class PayrollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.enterprise.modules.payroll'
    label = 'enterprise_module_payroll'
    verbose_name = 'enterprise module payroll'
