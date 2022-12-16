from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.association.modules.admin'
    label = 'association_module_admin'
    verbose_name = 'association module admin'
