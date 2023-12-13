from .models import Room


def select_all_rooms_data(request):
    data = {
        'all_rooms': Room.objects.all(),
    }
    return data
