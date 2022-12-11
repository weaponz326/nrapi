from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.enterprise.accounts'
    label = 'enterprise_account'
    verbose_name = 'enterprise account'
