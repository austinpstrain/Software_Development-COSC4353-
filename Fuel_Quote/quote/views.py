from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def quote(request):
    return render(request, "quote/form.html")


def history(request):
    return render(request, "quote/history.html")

def registerClient(request):
    return render(request,"quote/registerClient.html")

def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			login(request,user)
			return redirect('home')
		else:
			messages.info(request,'Username OR password is incorrect.')
			#return HttpResponse("Invalid login details given")
	else:
		return render(request, 'quote/login.html',{})
    

def profileManager(request):
    return render(request, "quote/profileManager.html")

def home(request):
    return render(request, "quote/home.html")
