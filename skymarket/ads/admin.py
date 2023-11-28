from django.contrib import admin

from ads.models import Ad, Comment

"""
Django admin configuration for managing Ads and Comments.

Registers the Ad and Comment models with the Django admin interface.
"""

admin.site.register(Ad)

admin.site.register(Comment)
