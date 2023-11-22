from django.shortcuts import render

from hotel.models import HeroSection, About,Testimony,MasterRoom,Menu


# Create your views here.

def master(request):
    # heroslider = HeroSection.objects.all()
    data = HeroSection.objects.all()
    return render(request,'master.html', {"slides": data})
def index(request):
    about = About.objects.all()[0]
    testimony = Testimony.objects.all()
    Mroom = MasterRoom.objects.all()
    rest = Menu.objects.all()
    context = {
        'nav': 'index',
        "abouts": about,
        "test":testimony,
        "room":Mroom,
        "restaurant":rest,
    }

    return render(request,"index.html", context)

def about(request):
    about = About.objects.all()[0]
    testimony = Testimony.objects.all()
    return render(request, 'about.html', {"nav": "about", "abouts": about, "test": testimony})

def blog(request):
    return render(request, 'blog.html', {'nav': 'blog'})

def contact(request):
    return render(request, 'contact.html', {'nav': 'contact'})

def rooms(request):
    Mroom = MasterRoom.objects.all()
    return render(request, 'rooms.html', {'nav': 'rooms', "room":Mroom})

def restaurant(request):
    rest = Menu.objects.all()
    return render(request, 'restaurant.html', {'nav': 'restaurant', "restaurant": rest})


def blog_single(request):
    return render(request, 'restaurant.html', {'nav': 'blog single'})

def rooms_single(request):
        return render(request, 'restaurant.html', {'nav': 'single rooms'})