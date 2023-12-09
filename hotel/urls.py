from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path("about/", views.AboutView.as_view(), name='about'),
    path("feedback/", views.FeedbackView.as_view(), name='feedback'),
    path("hotel_rooms/", views.HotelRoomsView.as_view(), name='hotelrooms'),
    path("room/<int:room_id>/", views.InDetailRoomView.as_view(), name='indetail'),
    path("in_detail_room/", views.InDetailRoomView.as_view(), name='indetail'),
    path('search_result/', views.SearchResultView.as_view(), name='search_result'),
    path('bookroom/', views.BookRoomView.as_view(), name='bookroom')
]
