from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already used')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registration successful!')
            return redirect('form')
    return render(request,"authentication/register.html")


def login_(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main1')  
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  
    return render(request,"authentication/login.html")
