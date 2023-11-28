from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    """
       Custom User admin to customize the display and functionality in the Django admin panel.
    """

    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name', 'phone')
    list_filter = ('role', )
