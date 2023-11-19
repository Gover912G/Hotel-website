from django.urls import path

from hotel import views

app_name = "hotel"
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('rooms/', views.rooms, name='rooms'),
    path('blog_single/', views.blog_single, name='blog single'),
    path('rooms_single/', views.rooms_single, name='rooms single'),

]