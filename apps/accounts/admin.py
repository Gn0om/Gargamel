from django.contrib import admin

from .models import Profile
#
# # admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
    )
    list_display_links = (
        'user',
        'id',
    )
    list_filter = (
        'user',
        'id',
    )
    search_fields = (
        'id',
        'user'
    )
