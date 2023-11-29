from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from register.forms import RegisterUserForm


# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('hotel:index') # Redirect to a success page.                ...
        else:
             messages.success(request, ("An error occurre please check your username and password"))# Return an 'invalid login' error message.
             return redirect('register:login')

    else:
        return render(request, 'authenticate/login.html', {'nav':'login'})

def logout_user(request):
    logout(request)
    return redirect('hotel:index')

def user_register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # phone = form.cleaned_data['phone']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,'registration successfully')
            return redirect('hotel:index')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/user_register.html',{'nav':'register', 'form':form})