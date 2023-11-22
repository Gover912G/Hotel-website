from django.urls import path

from hotel import views


app_name = "blogs"
urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog_single/', views.blog_single, name='blog single'),
]