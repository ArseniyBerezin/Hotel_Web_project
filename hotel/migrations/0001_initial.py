# Generated by Django 4.2.5 on 2023-10-29 13:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Стандарт', 'Стандарт'), ('Комфорт', 'Комфорт'), ('Семейный', 'Семейный'), ('Престиж', 'Престиж'), ('Бизнес класс', 'Бизнес класс'), ('Люкс', 'Люкс'), ('Люкс VIP', 'Люкс VIP')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('Стандарт', 'Стандарт'), ('Комфорт', 'Комфорт'), ('Семейный', 'Семейный'), ('Престиж', 'Престиж'), ('Бизнес класс', 'Бизнес класс'), ('Люкс', 'Люкс'), ('Люкс VIP', 'Люкс VIP')], max_length=256)),
                ('guests', models.CharField(choices=[('1 чел.', '1 чел.'), ('2 чел.', '2 чел.'), ('3 чел.', '3 чел.'), ('4 чел.', '4 чел.'), ('5 чел.', '5 чел.')], max_length=256)),
                ('number_of_beds', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('floor', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(15)])),
                ('room_image', models.ImageField(blank=True, null=True, upload_to='rooms_image')),
                ('price_night', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(10000)])),
                ('full_description', models.TextField(max_length=2048)),
            ],
        ),
    ]
