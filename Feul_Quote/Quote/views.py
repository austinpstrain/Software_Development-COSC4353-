from django.shortcuts import render, redirect
from django.http import HttpResponse
from Quote.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from .form import GetquoteForm, CreateUserForm, CustomerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
#from .decorators import unauthenticated_user,allowed_users, admin_only
from django.contrib.auth.decorators import login_required



# Create your views here.

def registerClient(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')


            messages.success(request, 'Account was created for ' + username)

            return redirect('login')
        

    context = {'form':form}
    return render(request, 'Quote/register.html', context)


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'Quote/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


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


def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'quote/account_settings.html', context)
