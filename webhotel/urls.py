from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from hotel import views as hotels_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hotel.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
