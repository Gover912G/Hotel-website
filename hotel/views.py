from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import FormView
# from rest_framework import request

from hotel.forms import AvailabilityForm
from hotel.models import HeroSection, About, Testimony, MasterRoom, Menu, Blogs, InstagramImage, Booking, Room
from manager.models import Book
from hotel.booking_function.availability import check_availability


# Create your views here.

def master(request):
    # heroslider = HeroSection.objects.all()
    data = HeroSection.objects.all()
    return render(request, 'master.html', {"slides": data})


def index(request):
    about = About.objects.all()[0]
    testimony = Testimony.objects.all()
    Mroom = MasterRoom.objects.all()
    rest = Menu.objects.all()
    blogs = Blogs.objects.all()
    insta = InstagramImage.objects.all()

    room = Room.objects.all()
    room_categories = Room.ROOM_CATEGORIES

    room_list = []
    for room_category, room_display in room_categories:
        # room_url = reverse('hotel:RoomBookingDetail', kwargs={'category': room_category})
        room_url = reverse('hotel:add_booking', kwargs={'category': room_category})
        room_list.append((room_display, room_url))

    context = {
        'nav': 'index',
        "abouts": about,
        "test": testimony,
        "room": Mroom,
        "restaurant": rest,
        "blog": blogs,
        "instagram": insta,
        "room_list": room_list,
    }

    return render(request, "index.html", context)


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
    return render(request, 'rooms.html', {'nav': 'rooms', "room": Mroom})


def restaurant(request):
    rest = Menu.objects.all()
    return render(request, 'restaurant.html', {'nav': 'restaurant', "restaurant": rest})


def blog_single(request):
    return render(request, 'restaurant.html', {'nav': 'blog single'})


def rooms_single(request):
    return render(request, 'restaurant.html', {'nav': 'single rooms'})


def add_booking(request):
    if request.method == 'POST':
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        room_type = request.POST.get('room')
        guests = request.POST.get('guest')

        books = Book(check_in=check_in, check_out=check_out, room_type=room_type, guests=guests)
        books.save()
        return redirect('/')

    return redirect('/')



class RoomBookingDetail(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=category)

        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.ROOM_CATEGORIES).get(room.category, None)
            context = {
                'room_category': room_category,
                'form': form,
            }
            return render(request, 'availability.html', context)
        else:
            return HttpResponse('Category does not exist')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse('All of this category of rooms are booked!! Try another one')


#
# from django.shortcuts import render
# from django.views import View
# from django.http import JsonResponse
#
# class RoomBookingDetail(View):
#     def post(self, request, *args, **kwargs):
#         category = self.kwargs.get('category', None)
#         room_list = Room.objects.filter(category=category)
#         form = AvailabilityForm(request.POST)
#         data = {}
#
#         if form.is_valid():
#             data = form.cleaned_data
#
#         available_rooms = [room for room in room_list if check_availability(room, data.get('check_in'), data.get('check_out'))]
#
#         if available_rooms:
#             room = available_rooms[0]
#             booking = Booking.objects.create(
#                 user=self.request.user,
#                 room=room,
#                 check_in=data.get('check_in'),
#                 check_out=data.get('check_out')
#             )
#             booking.save()
#             # Modify the response based on your needs (JSON, HTML, etc.)
#             return JsonResponse({'message': 'Booking successful', 'booking_details': {'room_number': room.number, 'check_in': data.get('check_in'), 'check_out': data.get('check_out')}})
#         else:
#             # Modify the response based on your needs (JSON, HTML, etc.)
#             return JsonResponse({'message': 'All rooms of this category are booked. Try another one'})
#




# class RoomBookingDetail(View):
#     def post(self, request, *args, **kwargs):
#         category = self.kwargs.get('category', None)
#         room_list = Room.objects.filter(category=category)
#         form = AvailabilityForm(request.POST)
#         data = {}  # Provide a default value for data
#
#         if form.is_valid():
#             data = form.cleaned_data
#
#         available_rooms = []
#         for room in room_list:
#             if check_availabilty(room, data.get('check_in'), data.get('check_out')):
#                 available_rooms.append(room)
#
#         if len(available_rooms) > 0:
#             room = available_rooms[0]
#             booking = Booking.objects.create(
#                 user=self.request.user,
#                 room=room,
#                 check_in=data.get('check_in'),
#                 check_out=data.get('check_out')
#             )
#             booking.save()
#             return HttpResponse((booking))
#         else:
#             return HttpResponse('All of this category of rooms are booked!! Try another one')


class AddBooking(FormView):
    form_class = AvailabilityForm
    template_name = 'availability.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])  # get a specific category of rooms
        available_rooms = []
        for room in room_list:  # check the available rooms for tha category
            if check_availabilty(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_in']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse(' Sorry the category of rooms you are looking are currently unavailable')
