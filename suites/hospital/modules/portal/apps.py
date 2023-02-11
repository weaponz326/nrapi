from django.apps import AppConfig


class PortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.hospital.modules.portal'
    label = 'hospital_module_portal'
    verbose_name = 'hospital module portal'
