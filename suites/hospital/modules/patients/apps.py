from django.apps import AppConfig


class PatientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.patients'
    label = 'hospital_module_patients'
    verbose_name = 'hospital module patients'
