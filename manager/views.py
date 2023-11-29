from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'indexx.html', {'navbar': 'indexx'})


def booking(request):
    return render(request, 'all-booking.html', {})


def add_booking(request):
    return render(request, 'add-booking.html', {})
