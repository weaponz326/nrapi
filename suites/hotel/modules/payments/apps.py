from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hotel.modules.payments'
    label = 'hotel_module_payments'
    verbose_name = 'hotel module payments'
