from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(null=True, blank=True, max_length=256)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name_of_hotel = models.CharField(max_length=128)
    prestige = models.CharField(max_length=32, unique=False)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f'Отель: {self.name_of_hotel} | Город: {self.city}'


class HotelRooms(models.Model):
    Hotel = Hotel()
    name = models.CharField(max_length=256)
    beds = models.IntegerField()
    floor = models.IntegerField()
    room_image = models.ImageField(upload_to="rooms_image", blank=True, null=True)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, null=True, blank=True)

    # def __str__(self):
    #     return f'Нормер: {self.name} | Отель: {self.Hotel.name_of_hotel}'


