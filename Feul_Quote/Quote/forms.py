from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from django.forms import ModelForm
from .models import PriceHistoryModule
from .models import UserProfile



class RegisterForm(UserCreationForm):

	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ('username', 'email','password1', 'password2')

	def save(self, commit=True):
		
		user = super().save(commit=False)
		user.email = self.cleaned_data['email']
		

		if commit:
			user.save()
		return user


class UserProfileFrom(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('fullname', 'address', 'city', 'state', 'zipcode')







class EditProfileForm(UserChangeForm):
	class Meta:
		model = UserProfile
		fields = ('fullname', 'address', 'city', 'state', 'zipcode')
		
	
class DateInput(forms.DateInput):
    input_type = 'date'

class FuelQuoteHistory(forms.ModelForm):
	class Meta:
		model = PriceHistoryModule
		fields = ['gallons_requested',  'delivery_date', 'delivery_address','suggested_price', 'total_due']
		widgets = {
		            'delivery_date': DateInput(),
		        }

	def save(self, commit=True):
		user = super().save(commit=False)
		user.gallons_requested = self.cleaned_data['gallons_requested']
		user.delivery_date = self.cleaned_data['delivery_date']
		user.delivery_address = self.cleaned_data['delivery_address']
		user.suggested_price = self.cleaned_data['suggested_price']
		user.total_due = self.cleaned_data['total_due']
		if commit:
			user.save()
		return user

	def clean_delivery_date(self):
		data = self.cleaned_data['delivery_date']

	
		if data < datetime.date.today():
			raise ValidationError(_('Invalid date - Date must be in the future'))

		

		return data

class FuelHistoryPage(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Write a post...'}))
	class Meta:
		model = PriceHistoryModule
		fields = ['gallons_requested',]


