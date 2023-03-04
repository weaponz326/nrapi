from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.admin'
    label = 'hospital_module_admin'
    verbose_name = 'hospital module admin'
