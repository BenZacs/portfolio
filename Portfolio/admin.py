from django.contrib import admin
from .models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):
    """Model for display event infomation in admin page."""
    list_display = (
        'company',
        'email'
    )

admin.site.register(Enquiry,EnquiryAdmin)