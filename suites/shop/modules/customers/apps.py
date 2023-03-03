from django.apps import AppConfig


class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.shop.modules.customers'
    label = 'shop_module_customers'
    verbose_name = 'shop module customers'
