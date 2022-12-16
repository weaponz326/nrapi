from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.enterprise.modules.employees'
    label = 'enterprise_module_employees'
    verbose_name = 'enterprise module employees'
