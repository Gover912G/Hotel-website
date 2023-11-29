from django.conf import settings
from django.db import models


# Create your models here.

class HeroSection(models.Model):
    text1 = models.CharField(default='', blank=False, max_length=100)
    text2 = models.CharField(default='', blank=False, max_length=100)
    image = models.ImageField(upload_to='hero')


class About(models.Model):
    subheadiing = models.CharField(default='subheading', blank=False, max_length=100)
    h2 = models.CharField(default="heading 2", blank=False, max_length=150)
    text = models.TextField(default='text', blank=False)
    text2 = models.CharField(max_length=100, blank=False)
    background1 = models.ImageField(upload_to='background', default='image')
    background2 = models.ImageField(upload_to='background', default='image')


class Testimony(models.Model):
    name = models.CharField(blank=False, max_length=100)
    position = models.CharField(max_length=50, default="")
    text = models.TextField(blank=False, default='text')
    image = models.ImageField(upload_to="testimonials")


class Menu(models.Model):
    name = models.CharField(blank=False, max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2, )
    text = models.TextField(blank=False, default='description')
    image = models.ImageField(upload_to='restaurant')


    def __int__(self):
        return self.name


class MasterRoom(models.Model):
    name = models.CharField(blank=False, max_length=30)
    price = models.DecimalField(blank=False, decimal_places=2, max_digits=7)
    image = models.ImageField(upload_to='master rooms')

    def __int__(self):
        return self.name
class Blogs(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, default='description')
    image = models.ImageField(upload_to='blogs')

class InstagramImage(models.Model):
    image = models.ImageField(upload_to='instagram images')



class Room(models.Model):
    ROOM_CATEGORIES = (
        ('KIN', 'King Room'),
        ('SUI', 'Suite Room'),
        ('DEL', 'Deluxe Room'),
        ('SUP', 'Superior Room'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField

    def __str__(self):
        return f'{self.number},{self.category} with {self.beds} beds for {self.capacity} adults'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room =models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

# models.py
class Book(models.Model):
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(auto_now_add=True)
    room_type = models.CharField(max_length=50)
    guests = models.CharField(max_length=50)
    # date_booked = models.DateTimeField(auto_now_add=True)
