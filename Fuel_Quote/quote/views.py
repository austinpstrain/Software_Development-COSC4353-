from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user
from django.urls import reverse
from urllib.parse import urlencode
# Create your views here.
from .models import *
from .forms import CreateUserForm, CustomerForm, QuoteForm
from .decorators import unauthenticated_user


@login_required(login_url='login')
def home(request, pk):
	customer = Customer.objects.get(id=pk)
	quotes = customer.quote_set.all() 
	form = QuoteForm(initial={'customer': customer})
	if request.method == 'POST':
		form = QuoteForm(request.POST)
		if form.is_valid():
			form.save()

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

            return redirect('home', 1)

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
            return redirect('home', 1) #pk param needs to be dynamic and return customer.id
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


def dashboard(request):
    quotes = Getquote.objects.all()
    total_requested = quotes.count()

    context = {'quotes': quotes, 'total_requested': total_requested}
    return render(request, 'Quote/overview.html', context)


def quote(request):
    quotes = Getquote.objects.all()

    quoteRequest = GetquoteForm()

    if request.method == 'POST':
        print('Printing POST:', request.POST)
        quoteRequest = GetquoteForm(request.POST)
        if quoteRequest.is_valid():
            quoteRequest.save()
            return redirect('/')

    context = {'quotes': quotes, 'quoteRequest': quoteRequest}
    return render(request, 'Quote/quote.html', context)


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    users = User.objects.all()
    quotes = customer.getquote_set.all()

    quotes_count = quotes.count()
    context = {'cusotmer': customer, 'quotes': quotes,
               'users': users, 'quotes_count': quotes_count}
    return render(request, 'Quote/customer.html', context)


def updateRequest(request):
    quoteRequest = GetquoteForm()
    context = {'quoteRequest': quoteRequest}
    return render(request, 'Quote/quote.html', context)


def quote_form(request):
    quoteRequest = GetquoteForm()

    # if request.method == 'POST':
    #     print('Printing POST:', request.POST)
    #     quoteRequest = GetquoteForm(request.POST)
    #     if quoteRequest.is_valid():
    #         quoteRequest.save()
    #         return redirect('/')

    context = {'quoteRequest': quoteRequest}
    return render(request, 'Quote/quote_form.html', context)
