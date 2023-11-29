from django.shortcuts import render, redirect

from hotel.models import HeroSection, About, Testimony, MasterRoom, Menu, Blogs, InstagramImage
from manager.models import Book


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
    blogs = Blogs.objects.all()
    insta = InstagramImage.objects.all()
    context = {
        'nav': 'index',
        "abouts": about,
        "test":testimony,
        "room":Mroom,
        "restaurant":rest,
        "blog": blogs,
        "instagram":insta,
    }

    return render(request,"index.html", context)

def about(request):
    about = About.objects.all()[0]
    testimony = Testimony.objects.all()
    return render(request, 'about.html', {"nav": "about", "abouts": about, "testi": testimony})

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


def add_booking(request):
    if request.method =='POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        room_type = request.POST.get('room')
        guests = request.POST.get('guest')

        books = Book(check_in=check_in, check_out=check_out, room_type=room_type,guests=guests)
        books.save()
        return redirect('/')


    return redirect('/')