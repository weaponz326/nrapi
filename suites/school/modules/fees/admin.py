from django.contrib import admin

from .models import Fees, FeesCodeConfig, FeesTarget


# Register your models here.

class FeesAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'fees_code', 'fees_name', 'fees_date')

class FeesTargetAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'fees', 'clase')

class FeesCodeConfigAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'prefix', 'suffix')

admin.site.register(Fees, FeesAdmin)
admin.site.register(FeesTarget, FeesTargetAdmin)
admin.site.register(FeesCodeConfig, FeesCodeConfigAdmin)
