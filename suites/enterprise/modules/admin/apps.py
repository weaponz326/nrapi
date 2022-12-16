from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.enterprise.modules.admin'
    label = 'enterprise_module_admin'
    verbose_name = 'enterprise module admin'
