from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.accounts'
    label = 'hospital_account'
    verbose_name = 'hospital account'
