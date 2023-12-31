from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from hotel import views as hotels_views
from hotel.views import *

router = routers.SimpleRouter()
router.register(r'room', RoomViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hotel.urls")),
    path("", include("users.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
