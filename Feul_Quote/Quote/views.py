from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, EditProfileForm, UserProfileFrom, FuelQuoteHistory, FuelHistoryPage
# from .forms import RegisterForm, EditProfileForm, FuelQuoteForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile, PriceHistoryModule
from django.http import HttpResponseRedirect



def index(request):
    
    return render(request, 'Quote/home.html')

def home(request):
     return render(request, 'Quote/home.html')
    

 
def fuelQuoteHistory(request):
   
    form = FuelHistoryPage()
  
    history_list = PriceHistoryModule.objects.filter(user=request.user)
    
    args ={'history_list': history_list}

    return render(request, 'Quote/fqh.html', args)

    
    


def register(request):
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
    return render(request, "Quote/clientRegistration.html", args)





def loginHome(request):
    return render(request, 'Quote/loginHome.html')

def profile(request):
    args = {'user': request.user}
    return render(request, 'Quote/clientProfile.html', args)

def editProfile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance=request.user)
        p_form = EditProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            return redirect('/clientProfile')

    else:
        form = EditProfileForm(instance=request.user)
        p_form = EditProfileForm(request.POST, instance=request.user.userprofile)
        args = {'form':form, 'p_form':p_form}
        return render(request, 'Quote/editProfile.html', args)


@login_required
def go_home_page(request):
    product = get_object_or_404(UserProfile)
    return render(request, 'Quote/loginHome.html', {'product' : product})




def fuelQuoteForm(request):
    history_list1 = PriceHistoryModule.objects.filter(user=request.user)
    if request.method == 'POST':
        
        form = FuelQuoteHistory(request.POST)
        
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.save()
            args = {"form":form, "history_list1":history_list1}
            return render(request, 'Quote/fqf.html', args )
       
    else:
        form = FuelQuoteHistory()
    return render(request, 'Quote/fqf.html', {"form":form, "history_list1":history_list1})


