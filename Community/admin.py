from django.contrib import admin
from .models import Community

# Register your models here.

class CommunityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Community_name',)}
    list_display = ('Community_name', 'slug')
admin.site.register(Community, CommunityAdmin)
