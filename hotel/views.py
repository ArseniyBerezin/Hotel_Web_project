from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from hotel.models import Room, Categories
from .forms import SearchForm
from django.urls import reverse


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
    context = {
        'Room': Room.objects.all(),
        'Categories': Categories.objects.all(),
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


def search_results(request):

    form = SearchForm(request.POST)
    rooms = Room.objects.all()

    if request.method == 'POST':
        print("POST")
        if form.is_valid():
            print("Valid")
            class_room = form.cleaned_data['class_room']
            guests = form.cleaned_data['guests']
            if class_room:
                rooms = rooms.filter(class_room=class_room)
            if guests:
                rooms = rooms.filter(guests=guests)

    context = {
        'room': rooms,
        'form': form,
        'Room': Room.objects.all()
    }

    return render(request, 'rooms/search_result.html', context)

