from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Quote.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .form import CreateUserForm
from django.contrib.auth.forms import UserCreationForm






def registerPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        profile_form = UserProfileFrom(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            return redirect("/home")
    else:
        form = RegisterForm()
        profile_form= UserProfileFrom()
    args = {"form":form, "profile_form":profile_form}
    return render(request, "Quote/register.html", args)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'Quote/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
     return render(request, 'Quote/home.html')


def index(request):
     return render(request, 'Quote/home.html')


