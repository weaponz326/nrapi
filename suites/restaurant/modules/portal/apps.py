from django.apps import AppConfig


class PortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.restaurant.modules.portal'
    label = 'restaurant_portal'
    verbose_name = 'restaurant module portal'
