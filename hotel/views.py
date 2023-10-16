from django.shortcuts import render

from hotel.models import Room


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
        'hotel_rooms': Room.objects.all(),
    }
    return render(request, 'rooms/hotelrooms.html', context)