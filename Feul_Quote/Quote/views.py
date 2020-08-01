from django.shortcuts import render, redirect
from django.http import HttpResponse
from Quote.models import *
from django.contrib.auth.models import User
from .form import GetquoteForm


# Create your views here.


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
