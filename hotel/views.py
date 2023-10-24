from django.shortcuts import render, get_object_or_404

from hotel.models import Room, Categories


def index(request):
    context = {
        'title': 'Test Title',
    }
    return render(request, 'rooms/index.html', context)


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
        'title': 'номера отеля',
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
