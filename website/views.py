from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']
        print(userName)
        print(password)
        user = authenticate(request, username= userName, password = password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been Logged In')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in, please try again...' )
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logged out')
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})
