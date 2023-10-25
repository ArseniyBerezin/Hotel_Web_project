# Generated by Django 4.2.5 on 2023-10-19 18:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='price_night',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(10000)]),
            preserve_default=False,
        ),
    ]