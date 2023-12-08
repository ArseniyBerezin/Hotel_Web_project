from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from hotel import views as hotels_views
from hotel.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hotel.urls")),
    path("", include("users.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('api/v1/roomlist', RoomAPIList.as_view()),
    path('api/v1/roomlist/<int:pk>', RoomAPIUpdate.as_view()),
    path('api/v1/roomdetail/<int:pk>', RoomAPIDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
