from django.forms import ModelForm

from manager.models import Book


class bookingForm(ModelForm):
    class Meta:
        model= Book
        # fields="__all__"
        fields = ('check_in', 'check_out', 'room_type', 'guests')

