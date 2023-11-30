from django import forms
from django.forms import ModelForm

from manager.models import Book


class bookingForm(ModelForm):
    class Meta:
        model= Book
        # fields="__all__"
        fields = ('check_in', 'check_out', 'room_type', 'guests')

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('KIN', 'King Room'),
        ('SUI', 'Suite Room'),
        ('DEL', 'Deluxe Room'),
        ('SUP', 'Superior Room'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(required=True,input_formats=['%Y-%m-%dT%H:%M'])
    check_out = forms.DateTimeField(required=True,input_formats=['%Y-%m-%dT%H:%M'])
