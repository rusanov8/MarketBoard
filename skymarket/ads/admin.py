from django.contrib import admin

from ads.models import Ad, Comment

from django.contrib import admin


@admin.register(Ad)
class UserAdmin(admin.ModelAdmin):
    """
        Admin configuration for the Ad model.
    """
    list_display = ('title', 'author')


@admin.register(Comment)
class UserAdmin(admin.ModelAdmin):
    """
        Admin configuration for the Comment model.
    """
    list_display = ('ad', 'text')

