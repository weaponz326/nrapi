from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.modules.orders'
    label = 'restaurant_module_orders'
    verbose_name = 'restaurant module orders'
