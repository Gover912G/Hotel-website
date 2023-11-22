from django.urls import path

from hotel import views


app_name = "rooms"
urlpatterns = [
    path('rooms/', views.rooms, name='rooms'),
    path('rooms_single/', views.rooms_single, name='rooms single'),
]