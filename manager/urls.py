from django.urls import path

from . import views



app_name = 'manager'
urlpatterns = [
    path('', views.index, name='dash'),
    path('booking', views.booking, name= 'booking'),
    path('add_booking', views.add_booking, name='add_booking'),
    path('all_booking', views.allbooking, name='all_booking'),
    path('edit_booking', views.edit_booking, name='edit_booking'),
    path('deletebooking<id>', views.deletebooking, name='delete_booking'),

]