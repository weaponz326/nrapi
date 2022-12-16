from django.apps import AppConfig


class AttendanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.enterprise.modules.attendance'
    label = 'enterprise_module_attendance'
    verbose_name = 'enterprise module attendance'
