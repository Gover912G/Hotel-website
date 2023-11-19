from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html", {'nav': 'index'})

def about(request):
    return render(request, 'about.html', {"nav": "about"})

def blog(request):
    return render(request, 'blog.html', {'nav': 'blog'})

def contact(request):
    return render(request, 'contact.html', {'nav': 'contact'})

def rooms(request):
    return render(request, 'rooms.html', {'nav': 'rooms'})

def restaurant(request):
        return render(request, 'restaurant.html', {'nav': 'restaurant'})


def blog_single(request):
    return render(request, 'restaurant.html', {'nav': 'blog single'})

def rooms_single(request):
        return render(request, 'restaurant.html', {'nav': 'single rooms'})