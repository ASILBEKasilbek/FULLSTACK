from django.contrib import admin
from .models import *


class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('subject', 'description', 'solution')

admin.site.register(SupportRequest, SupportRequestAdmin)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'video')
    search_fields = ('question', 'answer')