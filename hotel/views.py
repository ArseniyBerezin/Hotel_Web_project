from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from hotel.models import Room, Categories
from .forms import SearchForm

from rest_framework import generics
from hotel.serializers import SerializerRoom


def about(request):
    context = {
        'title': 'О нас'
    }
    return render(request, 'rooms/about.html', context)


def feedback(request):
    context = {
        'title': 'Обратная связь'
    }
    return render(request, 'rooms/feedback.html', context)


def hotel_rooms(request):
    room = Room.objects.all()
    categories = Categories.objects.all()

    context = {
        'Room': room,
        'Categories': categories,
    }

    return render(request, 'rooms/hotelrooms.html', context)


def in_detail_room(request, room_id):
    context = {
        'Room': Room.objects.all(),
        'room_id': get_object_or_404(Room, id=room_id),
    }
    return render(request, 'rooms/indetail.html', context)


def index(request):
    type_choices = Room.type_choices
    persons_choices = Room.persons_choices

    context = {
        'type_choices': type_choices,
        'persons_choices': persons_choices,
    }

    return render(request, 'rooms/index.html', context)


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


def book_room(request):
    context = {

    }
    return render(request, 'rooms/book.html', context)


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

