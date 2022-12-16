from django.contrib import admin

from .models import ReceivedLetter, SentLetter


# Register your models here.

class SentLetterAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'date_sent', 'reference_number', 'subject', 'recepient')

class ReceivedLetterAdmin(admin.ModelAdmin):
    list_display = ('pkid', 'id', 'created_at', 'date_received', 'reference_number', 'subject', 'sender')

admin.site.register(SentLetter, SentLetterAdmin)
admin.site.register(ReceivedLetter, ReceivedLetterAdmin)
