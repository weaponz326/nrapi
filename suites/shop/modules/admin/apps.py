from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.shop.modules.admin'
    label = 'shop_module_admin'
    verbose_name = 'shop module admin'
