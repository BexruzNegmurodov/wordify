from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages

from .forms import MyLogin, MyRegistration


def mylogin(request):
    form = MyLogin()
    if request.user.is_authenticated:
        return redirect('main:home')
    if request.method == "POST":
        form = MyLogin(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:home')
    ctx = {
        'form': form
    }
    return render(request, 'profile/login.html', ctx)


def mylogaut(request):
    if not request.user.is_authenticated:
        return redirect('main:home')
    if request.method == "POST":
        messages.success(request, f"Logged out\nThanks for spending some quality time with the web site today.")
        logout(request)
        return redirect('profiles:login')
    return render(request, 'profile/logaut.html')


def myregistration(request):
    form = MyRegistration()
    if request.user.is_authenticated:
        return redirect('main:home')
    if request.method == 'POST':
        form = MyRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles:login')
    ctx = {
        'form': form
    }
    return render(request, 'profile/registration.html', ctx)
