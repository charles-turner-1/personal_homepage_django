from django.contrib import admin

from .models import FullEnquiry, SimpleEnquiry


class SimpleEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'date')
# Register your models here.
admin.site.register(FullEnquiry)
admin.site.register(SimpleEnquiry, SimpleEnquiryAdmin)