from django.shortcuts import render, get_object_or_404
from hotel.models import Room, Categories
from .forms import SearchForm


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


def search_results(request):

    form = SearchForm(request.POST)
    rooms = Room.objects.all()

    if request.method == 'POST':
        print("POST")
        if form.is_valid():
            print("Valid")
            room_class = form.cleaned_data['room_class']
            guests = form.cleaned_data['guests']
            if room_class:
                rooms = rooms.filter(room_class=room_class)
            if guests:
                rooms = rooms.filter(guests=guests)

    context = {
        'room': rooms,
        'form': form,
        'Room': Room.objects.all(),
    }

    return render(request, 'rooms/search_result.html', context)

