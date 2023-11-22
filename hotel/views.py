from django.shortcuts import render

from hotel.models import HeroSection, About,Testimony,MasterRoom


# Create your views here.

def master(request):
    # heroslider = HeroSection.objects.all()
    data = HeroSection.objects.all()
    return render(request,'master.html', {"slides": data})

def index(request):
    about = About.objects.all()[0]
    testimony = Testimony.objects.all()
    Mroom = MasterRoom.objects.all()
    return render(request,"index.html", {'nav': 'index', "abouts": about, "test":testimony, "room":Mroom})

def about(request):
    about = About.objects.all()[0]
    testimony = Testimony.objects.all()
    return render(request, 'about.html', {"nav": "about", "abouts": about, "test": testimony})

def contact(request):
    return render(request, 'contact.html', {'nav': 'contact'})

def restaurant(request):
        return render(request, 'restaurant.html', {'nav': 'restaurant'})




