from django.apps import AppConfig


class BillsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.bills'
    label = 'hospital_module_bills'
    verbose_name = 'hospital module bills'
