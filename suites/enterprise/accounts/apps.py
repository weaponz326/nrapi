from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.accounts'
    label = 'restaurant_account'
    verbose_name = 'restaurant account'
