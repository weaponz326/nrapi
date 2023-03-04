from django.apps import AppConfig


class InventoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.shop.modules.inventory'
    label = 'shop_module_inventory'
    verbose_name = 'shop module inventory'
