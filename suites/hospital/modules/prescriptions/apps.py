from django.apps import AppConfig


class PrescriptionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.prescriptions'
    label = 'hospital_module_prescriptions'
    verbose_name = 'hospital module prescriptions'
