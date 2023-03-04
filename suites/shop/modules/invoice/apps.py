from django.apps import AppConfig


class InvoiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.shop.modules.invoice'
    label = 'shop_module_invoice'
    verbose_name = 'shop module invoice'
