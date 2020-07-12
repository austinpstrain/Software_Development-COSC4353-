from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CustomerForm(ModelForm):
	#password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']
		

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		widgets = {
      'password1': forms.PasswordInput()
         }



class QuoteForm(ModelForm):
	class Meta:
		model = Quote
		fields = '__all__'
		exclude = ['total_amount']