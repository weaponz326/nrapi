from django.apps import AppConfig


class AttendanceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suites.school.modules.attendance'
    label = 'school_module_attendance'
    verbose_name = 'school module attendance'
