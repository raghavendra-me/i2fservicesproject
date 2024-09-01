from django.contrib import admin
from .models import Contact, Service

class ContactAdmin(admin.ModelAdmin):
    list_display = ('uuid','name', 'phone_number', 'email', 'city_from','get_services_needed',  'how_did_you_hear_about_us')
    search_fields = ('name','uuid' )
    # Add other customizations if needed
    def get_services_needed(self, obj):
        return ", ".join([service.name for service in obj.services_needed.all()])
    get_services_needed.short_description = 'Services Needed'

admin.site.register(Contact, ContactAdmin)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
