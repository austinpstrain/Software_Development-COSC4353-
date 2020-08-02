import unittest
#from fuelpredictionsystem import registration
from django.test import TestCase
from fuelpredictionsystem.forms import FuelQuoteHistory



class TestPriciModule(TestCase):
  
	def test_get_quote(self):
    	# test invalid data
	    invalid_data = {
		  "gallons_requested" : "",
		  "delivery_date" : "",
		  "delivery_address" : "" 
	    }
	    form = FuelQuoteHistory(data=invalid_data)
	    form.is_valid()
	    self.assertTrue(form.errors)


	    valid_data = {
		  "gallons_requested" : "1000",
		  "delivery_date" : "05-30-2020",
		  "delivery_address" : "Texas" 
	    }
	    form = FuelQuoteHistory(data=valid_data)
	    form.is_valid()
	    self.assertTrue(form.errors)