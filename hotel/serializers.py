from rest_framework import serializers
from hotel.models import Room, Categories


class SerializerRoom(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

    def create(self, validate_data):
        return Room.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get("name", instance.name)
        instance.room_class = validate_data.get("room_class", instance.room_class)
        instance.guests = validate_data.get("guests", instance.guests)
        instance.number_of_beds = validate_data.get("number_of_beds", instance.number_of_beds)
        instance.floor = validate_data.get("floor", instance.floor)
        instance.price_night = validate_data.get("price_night", instance.price_night)
        instance.full_description = validate_data.get("full_description", instance.full_description)
        instance.reservation = validate_data.get("reservation", instance.reservation)
        instance.check_in = validate_data.get("check_in", instance.check_in)
        instance.check_out = validate_data.get("check_out", instance.check_out)
        instance.save()
        return instance
