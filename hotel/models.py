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
    PERSON_1 = "1 чел."
    PERSON_2 = "2 чел."
    PERSON_3 = "3 чел."
    PERSON_4 = "4 чел."
    PERSON_5 = "5 чел."
    persons_choices = (
        (PERSON_1, "1 чел."),
        (PERSON_2, "2 чел."),
        (PERSON_3, "3 чел."),
        (PERSON_4, "4 чел."),
        (PERSON_5, "5 чел."),
    )

    name = models.CharField(max_length=256)
    room_class = models.CharField(max_length=256, choices=type_choices)
    guests = models.CharField(max_length=256, choices=persons_choices)
    number_of_beds = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    floor = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    room_image = models.ImageField(upload_to="rooms_image", blank=True, null=True)
    price_night = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(10000)])
    full_description = models.TextField(max_length=2048)

    def __str__(self):
        return f"№{self.pk}: Комната '{self.name}' типа {self.room_class} | цена/ночь: {self.price_night}"


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

    def __str__(self):
        return f"Категория:{self.name}"


