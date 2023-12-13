from django.urls import path
from . import views
from .views import profile_view, login_view, registration_view
from django.contrib.auth import views as auth_views

urlpatterns = [

    path("profile", profile_view, name="profile"),
    path("registration", registration_view, name="registration"),
    path("login", login_view, name="login"),
    path("exit/", auth_views.LogoutView.as_view(), name='exit'),
]

