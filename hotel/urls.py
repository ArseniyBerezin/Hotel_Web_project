from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about/", views.about, name='about'),
    path("feedback/", views.feedback, name='feedback'),
    path("hotel_rooms/", views.hotel_rooms, name='hotelrooms'),
]