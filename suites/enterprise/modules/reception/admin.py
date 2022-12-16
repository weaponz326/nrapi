from django.contrib import admin

from .models import Visitor


# Register your models here.

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'account', 'visit_code', 'visit_date', 'visitor_name', 'visitor_phone')

admin.site.register(Visitor, VisitorAdmin)
