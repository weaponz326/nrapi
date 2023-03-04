from django.apps import AppConfig


class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.shop.modules.payments'
    label = 'shop_module_payments'
    verbose_name = 'shop module payments'
