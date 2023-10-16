from django.contrib import admin
from django.urls import path, include

from hotel import views as hotels_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hotel.urls")),
]
