from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'price', 'stock', 'community', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('event_name',)}

admin.site.register(Event, EventAdmin)
