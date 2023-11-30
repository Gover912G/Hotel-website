from django.shortcuts import render

from hotel.models import Booking


# Create your views here.

def index(request):
    bookings = Booking.objects.all()
    context={
        'navbar': 'indexx',
        "books":bookings,
    }
    return render(request, 'indexx.html', context)


def booking(request):
    bookings= Booking.objects.all()
    return render(request, 'all-booking.html', {"books":bookings})


def add_booking(request):
    return render(request, 'add-booking.html', {})

def edit_booking(request):
    return render(request, 'edit-booking.html', {})


def deletebooking(request, id):
    bookings = Booking.objects.get(id=id)
    bookings.delete()
    return render(request,'indexx.html')