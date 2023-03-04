from django.apps import AppConfig


class NursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.nurses'
    label = 'hospital_module_nurses'
    verbose_name = 'hospital module nurses'
