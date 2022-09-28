from django.apps import AppConfig


class KitchenStockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.modules.kitchen_stock'
    label = 'restaurant_module_kitchen_stock'
    verbose_name = 'restaurant module kitchen stock'
