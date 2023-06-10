from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
import os
from django.views.static import serve

print(os.path.abspath(__file__))


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    path("users/", include("users.urls")),
    path("workouts/", include("workouts.urls")),
    path("obiettivi/", include("obiettivi.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    re_path(r'^media/(?P<path>.)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)