from django.db import models

# Create your models here.
class Book(models.Model):
    check_in = models.DateTimeField(null=False)
    check_out = models.DateTimeField(null=False)
    room_type = models.CharField(max_length=50)
    guests = models.CharField(max_length=50)
