import unittest
#from fuelpredictionsystem import registration
from django.test import TestCase
from fuelpredictionsystem.forms import RegisterForm
# Create your tests here.


class TestRegistrationForm(TestCase):
  
	def test_registration_form(self):
    	# test invalid data
	    invalid_data = {
	      "username": "",
		  "first_name" : "",
		  "last_name" : "",
		  "email" : "",
		  "phone" : "",
		  "city" : "",
		  "state" : "",
		  "password1" : "",
		  "password2" : ""
	    }
	    form = RegisterForm(data=invalid_data)
	    form.is_valid()
	    self.assertTrue(form.errors)


	    #test valid data
	    valid_data = {
	      "username": "anna1",
		  "first_name" : "anna", 
		  "last_name" : "fariha",
		  "email" : "anna@gmail.com",
		  "phone" : "12345678",
		  "city" : "Houston",
		  "state" : "Tx",
		  "password1" : "efuvalona1",
		  "password2" : "efuvalona1"
	    }
	    form = RegisterForm(data=valid_data)
	    form.is_valid()
	    self.assertFalse(form.errors)



