from django.db import models

# Create your models here.
class Book(models.Model):
    check_in = models.DateTimeField(null=False,default='')
    check_out = models.DateTimeField(null=False, default='')
    room_type = models.CharField(max_length=50)
    guests = models.CharField(max_length=50)

class RoomCategory(models.Model):
    category = models.CharField(max_length=50)
    rate = models.FloatField()

    def __str__(self):
        return self.category


class Room(models.Model):
    number = models.IntegerField()
    beds = models.IntegerField()
    capacity = models.IntegerField()
    category = models.ForeignKey(
        RoomCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.number}. Beds = {self.beds} People = {self.capacity}'