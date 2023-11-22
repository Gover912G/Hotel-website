from django.shortcuts import render

from hotel.models import MasterRoom


# Create your views here.
def rooms(request):
    Mroom = MasterRoom.objects.all()
    return render(request, 'rooms.html', {'nav': 'rooms', "room":Mroom})

def rooms_single(request):
    return render(request, 'rooms-single.html', {'nav': 'single rooms'})