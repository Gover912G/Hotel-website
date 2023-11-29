from django.urls import path

from . import views



app_name = 'register'
urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name= 'logout'),
    path('register_user', views.user_register, name='register'),

]