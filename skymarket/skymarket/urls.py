from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('api/', include('users.urls', namespace='users')),
    path('api/', include('ads.urls', namespace='ads')),
    path("__debug__/", include("debug_toolbar.urls")),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
