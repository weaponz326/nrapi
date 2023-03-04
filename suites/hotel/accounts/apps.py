from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hotel.accounts'
    label = 'hotel_account'
    verbose_name = 'hotel account'
