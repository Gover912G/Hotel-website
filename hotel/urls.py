from django.urls import path

from hotel import views

app_name = "hotel"
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('restaurant/', views.restaurant, name='restaurant'),
]