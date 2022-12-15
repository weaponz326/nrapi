from django.apps import AppConfig


class LedgerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.enterprise.modules.ledger'
    label = 'enterprise_module_ledger'
    verbose_name = 'enterprise module ledger'
