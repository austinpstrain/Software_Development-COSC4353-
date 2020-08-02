import unittest
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
	      "username": "sam",
		  "first_name" : "sam", 
		  "last_name" : "sammy",
		  "email" : "sam@gmail.com",
		  "phone" : "71355555",
		  "city" : "Houston",
		  "state" : "Tx",
		  "password1" : "cosc4353sum",
		  "password2" : "cosc4353sum"
	    }
	    form = RegisterForm(data=valid_data)
	    form.is_valid()
	    self.assertFalse(form.errors)



