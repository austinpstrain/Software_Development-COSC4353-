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
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method=='POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
		
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				messages.info(request,'Username OR password is incorrect.')
	
	context={}
	return render(request, 'quote/login.html',context)
    

def profileManager(request):
    return render(request, "quote/profileManager.html")

def home(request):
    return render(request, "quote/home.html")
