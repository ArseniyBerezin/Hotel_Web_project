from django.contrib import admin

from rooms.models import HotelRooms, Categories, Hotel


admin.site.register(HotelRooms)
admin.site.register(Categories)
admin.site.register(Hotel)

