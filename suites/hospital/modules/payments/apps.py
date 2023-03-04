from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.payments'
    label = 'hospital_module_payments'
    verbose_name = 'hospital module payments'
