from cProfile import label
from django.apps import AppConfig


class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.modules.customers'
    label = 'restaurant_module_customers'
    verbose_name = 'restaurant module customers'
