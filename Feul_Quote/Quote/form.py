from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class GetquoteForm(ModelForm):
    class Meta:
        model = Getquote
        fields = ['customer', 'gallons_requested', 'Address_1', 'state',
                  'delivery_date', 'suggested_price']
class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']