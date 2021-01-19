from django.contrib import admin
from .models import Info

class InfoAdmin(admin.ModelAdmin):
    """Model for display event infomation in admin page."""
    list_display = (
        'first_name',
        'last_name',
        'phone_number',
    )

admin.site.register(Info,InfoAdmin)