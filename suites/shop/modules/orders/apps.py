from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.shop.modules.orders'
    label = 'shop_module_orders'
    verbose_name = 'shop module orders'
