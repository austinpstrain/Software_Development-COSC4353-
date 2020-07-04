from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user

# Create your views here.
from .models import *
from .forms import CreateUserForm, CustomerForm, QuoteForm
from .decorators import unauthenticated_user

""" def quote(request, pk):
	customer = Customer.objects.get(id=pk)
	quotes = customer.quote_set.all() 
	context = {'customer' : customer, 'quotes' : quotes}
	return render(request, "quote/form.html", context)

def history(request, pk):
	customer = Customer.objects.get(id=pk)
	quotes = customer.quote_set.all() 
	context = {'customer' : customer, 'quotes' : quotes}
	return render(request, "quote/history.html", context) """
@login_required(login_url='login')
def home(request, pk):
	form = QuoteForm()
	if request.method == 'POST':
		form = QuoteForm(request.POST)
		if form.is_valid():
			form.save()
	customer = Customer.objects.get(id=pk)
	quotes = customer.quote_set.all() 
	context = {'customer' : customer, 'quotes' : quotes, 'form' : form}
	return render(request, 'quote/home.html', context)


@login_required(login_url='login')
def profileManager(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Profile was created for ' + username)

            return redirect('home')

    context = {'form': form}
    return render(request, 'quote/home.html', context)

@unauthenticated_user
def registerClient(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'quote/registerClient.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'quote/login.html', context)

	


def logoutUser(request):
	logout(request)
	return redirect('login')



@login_required(login_url='login')
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'quote/account_settings.html', context)


@login_required(login_url='login')
def userPage(request):
    context = {}
    return render(request, 'quote/user.html')


@login_required(login_url='login')
def customer(request):

    return render(request, 'quote/customer.html')



