from django.urls import path
from . import views
from .views import profile_view, login_view, registration_view

urlpatterns = [

    path("profile", profile_view, name="profile"),
    path("registration", registration_view, name="registration"),
    path("login", login_view, name="login"),
]
