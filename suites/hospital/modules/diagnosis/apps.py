from django.apps import AppConfig


class DiagnosisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.diagnosis'
    label = 'hospital_module_diagnosis'
    verbose_name = 'hospital module diagnosis'
