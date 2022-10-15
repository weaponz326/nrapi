from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.school.modules.payments'
    label = 'school_module_payments'
    verbose_name = 'school module payments'
