from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.modules.payments'
    label = 'restaurant_module_payments'
    verbose_name = 'restaurant module payments'
