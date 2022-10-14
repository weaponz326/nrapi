from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.school.modules.admin'
    label = 'school_module_admin'
    verbose_name = 'school module admin'
