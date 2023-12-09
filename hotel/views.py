from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.response import Response

from hotel.models import Room, Categories
from .forms import SearchForm

from rest_framework import generics
from hotel.serializers import SerializerRoom


class AboutView(View):
    template_name = 'rooms/about.html'

    def get(self, request):
        context = {
            'title': 'О нас'
        }
        return render(request, self.template_name, context)


class FeedbackView(View):
    template_name = 'rooms/feedback.html'

    def get(self, request):
        context = {
            'title': 'Обратная связь'
        }
        return render(request, self.template_name, context)


class HotelRoomsView(View):
    template_name = 'rooms/hotelrooms.html'

    def get(self, request):
        room = Room.objects.all()
        categories = Categories.objects.all()

        context = {
            'Room': room,
            'Categories': categories,
        }

        return render(request, self.template_name, context)


class InDetailRoomView(View):
    template_name = 'rooms/indetail.html'

    def get(self, request, room_id):
        context = {
            'Room': Room.objects.all(),
            'room_id': get_object_or_404(Room, id=room_id),
        }
        return render(request, self.template_name, context)


class IndexView(View):
    template_name = 'rooms/index.html'

    def get(self, request):
        type_choices = Room.type_choices
        persons_choices = Room.persons_choices

        context = {
            'type_choices': type_choices,
            'persons_choices': persons_choices,
        }

        return render(request, self.template_name, context)


class SearchResultView(View):
    template_name = 'rooms/search_result.html'

    def post(self, request, *args, **kwargs):
        rooms = Room.objects.all()
        form = SearchForm(request.POST)
        if form.is_valid():
            room_class = form.cleaned_data['room_class']
            guests = form.cleaned_data['guests']
            if room_class:
                rooms = rooms.filter(room_class=room_class)
            if guests:
                rooms = rooms.filter(guests=guests)

            return render(request, self.template_name, {'room': rooms, 'form': form, 'Room': Room.objects.all()})


class BookRoomView(View):
    template_name = 'rooms/book.html'

    def get(self, request):
        context = {

        }
        return render(request, self.template_name, context)


class RoomAPIList(generics.ListCreateAPIView):

    """ Methods GET POST """

    queryset = Room.objects.all()
    serializer_class = SerializerRoom


class RoomAPIUpdate(generics.UpdateAPIView):

    """Methods PUT PATCH """

    queryset = Room.objects.all()
    serializer_class = SerializerRoom


class RoomAPIDetailView(generics.RetrieveUpdateDestroyAPIView):

    """Methods GET PUT PATCH DELETE"""

    queryset = Room.objects.all()
    serializer_class = SerializerRoom

