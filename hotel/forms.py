from django import forms
from hotel.models import Room
from django.forms import ModelForm


class SearchForm(forms.Form, ModelForm):
    room_class = forms.ChoiceField(
        label='Класс номера',
        choices=Room.type_choices,
        required=True
    )

    guests = forms.ChoiceField(
        label='Количество человек',
        choices=Room.persons_choices,
        required=True
    )

    class Meta:
        model = Room
        fields = ('room_class', 'guests')
