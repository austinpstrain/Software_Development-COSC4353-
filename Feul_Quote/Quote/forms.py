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
		# user = super(RegisterForm, self).save(commit=False)
		user = super().save(commit=False)
		user.email = self.cleaned_data['email']
		# user.phone = self.cleaned_data['phone']
		# user.city = self.cleaned_data["city"]
		# user.state = self.cleaned_data["state"]

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
		# fields = ('email', 'first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'password')


# class EditProfileForm(UserChangeForm):
# 	class Meta:
# 		model = User
# 		fields = ('email', 'first_name', 'last_name', 'password')
# 		# fields = ('email', 'first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'password')
	
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

		# Check if a date in not in the past
		if data < datetime.date.today():
			raise ValidationError(_('Invalid date - Date must be in the future'))

		# Check if data is not the current day
		# if data == datetime.data.today():
		# 	raise ValidationError(_('Invalid date - Date must be in the future'))

		return data

class FuelHistoryPage(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Write a post...'}))
	class Meta:
		model = PriceHistoryModule
		fields = ['gallons_requested',]


# class  FuelQuoteForm(forms.Form):
# 	class Meta:
# 		model = User
# 		fields = ["gallons_requested", "delivery_date", "delivery_address", "suggested_price", "total_due"]

# 	gallons_requested = forms.IntegerField( 
# 		required=True, 
# 		max_value=10000, 
# 		min_value=1
# 		)
	
# 	delivery_date = forms.DateField(
# 		required=True,
# 		localize=True,
# 		widget=forms.DateInput(format='%m/%d/%Y', attrs={
# 			'class': 'form-control datetimepicker-input',
# 			'data-target': '#datetimepicker1'}),
# 		input_formats='%m/%d/%Y'
# 	)

# 	delivery_address = forms.CharField(required=True)
# 	suggested_price = forms.FloatField()
# 	total_due = forms.FloatField()


# 	def clean_delivery_date(self):
# 		data = self.cleaned_data['delivery_date']

# 		# Check if a date in not in the past
# 		if data < datetime.date.today():
# 			raise ValidationError(_('Invalid date - Date must be in the future'))

# 		# Check if data is not the current day
# 		if data == datetime.data.today():
# 			raise ValidationError(_('Invalid date - Date must be in the future'))

# 		return data

	# def save(self, commit=True):
	# 	user = super(FuelQuoteForm, self).save(commit=False)
	# 	user.gallons_requested = self.cleaned_data['gallons_requested']
	# 	user.delivery_date = self.cleaned_data['delivery_date']
	# 	user.delivery_address = self.cleaned_data['delivery_address']
	# 	user.location = self.cleaned_data['location']
	# 	user.season = self.cleaned_data['season']

	# 	if commit:
	# 		user.save()
	# 	return user


# class  FuelQuoteForm(forms.ModelForm):
#     error_css_class = 'error'
#     location = forms.ChoiceField(choices=STATE, required=True )
#     season = forms.ChoiceField(choices=SEASON, required=True )
#     class Meta:
#     	model = PriceModule
#     	fields = ["gallons_requested", "delivery_date", "delivery_address", "location", "season"]

	# def save(self, commit=True):
	# 	PriceModule = super(FuelQuoteForm, self).save(commit=False)
	# 	PriceModule.gallons_requested = self.cleaned_data['gallons_requested']
	# 	PriceModule.delivery_date = self.cleaned_data['delivery_date']
	# 	PriceModule.delivery_address = self.cleaned_data['delivery_address']
	# 	PriceModule.location = self.cleaned_data['location']
	# 	PriceModule.season = self.cleaned_data['season']

	# 	if commit:
	# 		PriceModule.save()
	# 	return PriceModule

