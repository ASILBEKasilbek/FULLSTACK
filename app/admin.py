from django.contrib import admin
from .models import *

admin.site.register(FAQ)


class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('subject', 'description', 'solution')

admin.site.register(SupportRequest, SupportRequestAdmin)
