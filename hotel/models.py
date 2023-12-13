from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Room(models.Model):

    TYPE_STANDARD = "Стандарт"
    TYPE_COMFORT = "Комфорт"
    TYPE_FAMILY = "Семейный"
    TYPE_PRESTIGE = "Престиж"
    TYPE_BUSINESS = "Бизнес класс"
    TYPE_LUXE = "Люкс"
    TYPE_LUXE_VIP = "Люкс VIP"
    type_choices = (
        (TYPE_STANDARD, "Стандарт"),
        (TYPE_COMFORT, "Комфорт"),
        (TYPE_FAMILY, "Семейный"),
        (TYPE_PRESTIGE, "Престиж"),
        (TYPE_BUSINESS, "Бизнес класс"),
        (TYPE_LUXE, "Люкс"),
        (TYPE_LUXE_VIP, "Люкс VIP"),
    )

    PERSON_1 = "1"
    PERSON_2 = "2"
    PERSON_3 = "3"
    PERSON_4 = "4"
    PERSON_5 = "5"
    persons_choices = (
        (PERSON_1, "1"),
        (PERSON_2, "2"),
        (PERSON_3, "3"),
        (PERSON_4, "4"),
        (PERSON_5, "5"),
    )

    name = models.CharField(max_length=256)
    room_class = models.CharField(max_length=256, choices=type_choices)
    guests = models.CharField(max_length=256, choices=persons_choices)
    number_of_beds = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    floor = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    room_image = models.ImageField(upload_to="rooms_image", blank=True, null=True)
    price_night = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(10000)])
    full_description = models.TextField(max_length=2048)
    reservation = models.BooleanField(default=False)
    check_in = models.DateField(default=None, null=True, blank=True)
    check_out = models.DateField(default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.reservation:
            free_rooms_count = Room.objects.filter(room_class=self.room_class, reservation=False).count()
            category_instance, created = Categories.objects.get_or_create(name=self.room_class)
            category_instance.free_rooms = free_rooms_count
            category_instance.free_rooms += 1
            category_instance.save()
        else:
            category_instance, created = Categories.objects.get_or_create(name=self.room_class)
            category_instance.free_rooms -= 1
            category_instance.save()

        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return f"№{self.pk}: Комната '{self.name}' типа {self.room_class} | цена/ночь: {self.price_night} | Бронь: {self.reservation}"


class Categories(models.Model):
    TYPE_STANDARD = "Стандарт"
    TYPE_COMFORT = "Комфорт"
    TYPE_FAMILY = "Семейный"
    TYPE_PRESTIGE = "Престиж"
    TYPE_BUSINESS = "Бизнес класс"
    TYPE_LUXE = "Люкс"
    TYPE_LUXE_VIP = "Люкс VIP"
    type_choices = (
        (TYPE_STANDARD, "Стандарт"),
        (TYPE_COMFORT, "Комфорт"),
        (TYPE_FAMILY, "Семейный"),
        (TYPE_PRESTIGE, "Престиж"),
        (TYPE_BUSINESS, "Бизнес класс"),
        (TYPE_LUXE, "Люкс"),
        (TYPE_LUXE_VIP, "Люкс VIP"),
    )

    name = models.CharField(max_length=64, choices=type_choices)
    free_rooms = models.IntegerField(default=0)

    def __str__(self):
        return f"Категория:{self.name} | Свободных данной категории: {self.free_rooms}"


