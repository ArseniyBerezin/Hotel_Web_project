# Generated by Django 4.2.5 on 2023-12-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_alter_room_check_in_alter_room_check_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=256),
        ),
        migrations.AlterField(
            model_name='room',
            name='reservation',
            field=models.BooleanField(default=False),
        ),
    ]
