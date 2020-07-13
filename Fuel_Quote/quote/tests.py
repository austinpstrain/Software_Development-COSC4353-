from django.test import TestCase
import pytest
from quote.models import Customer, Quote, Pricing
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

# Create your tests here.

'''
#python manage.py test
class TestCustomerModel(TestCase):

	def setUp(self):
		self.customer1 = Customer.objects.create(
			First_name = "John", Last_name="Smith", City = "Houston" , Address_1 = "123 fake street"

			)

	def test_customer_name(self):
		self.assertEqual(self.customer1.First_name, "John")


	def test_customer_city(self):
		self.assertEqual(self.customer1.City, "Houston")

	def test_customer_address_1(self):
		self.assertEqual(self.customer1.Address_1, "123 fake street")


	def test_str_return(self):
		self.assertEqual(str(self.customer1),"John")


'''

#Mixers 
'''
class TestCustomerModel(TestCase):

	def test_customer_name(self):
		customer1 = mixer.blend(Customer, First_name = 'John')
		cust_result = Customer.objects.last()
		self.assertEqual(cust_result.First_name, "John")

	def test_customer_city(self):
		city = mixer.blend(Customer, City ="Houston")
		city_result = Customer.objects.last()
		self.assertEqual(city_result.City, "Houston")


'''

	#pytest
	#cmd pytest -v
'''
class TestCustomerModel(TestCase):

	def test_customer_name(self):
		customer1 = mixer.blend(Customer, First_name = 'John')
		cust_result = Customer.objects.last()
		assert cust_result.First_name == "John"
		

	def test_customer_city(self):
		city = mixer.blend(Customer, City ="Houston")
		city_result = Customer.objects.last()
		assert city_result.City == "Houston"

	def test_str_return(self):
		name = mixer.blend(Customer, First_name="John")
		cust_result = Customer.objects.last()
		assert str(cust_result) == "John"

'''

#Code Coverage
#cmd pytest --cov=. --cov-report=html

'''
class TestCustomerModel(TestCase):

	def test_customer_name(self):
		customer1 = mixer.blend(Customer, First_name = 'Joh')
		cust_result = Customer.objects.last()
		assert cust_result.First_name == "First_name"
		

	def test_customer_city(self):
		city = mixer.blend(Customer, City ="Houston")
		city_result = Customer.objects.last()
		assert city_result.City == "Houston"

	def test_str_return(self):
		name = mixer.blend(Customer, First_name="John")
		cust_result = Customer.objects.last()
		assert str(cust_result) == "John"

'''

'''
class TestPricingModel:
	def test_str_return(self):
		nam = mixer.blend(Pricing, name = "John")
		nam_result = Pricing.objects.last()
		assert str(nam_result) == "John"

	def test_sugg_pri(self):
		price = mixer.blend(Pricing, suggested_price = 1.89)
		pri_result = Pricing.objects.last()
		assert pri_result == 1.89


'''


class TestHome(TestCase):

	class TestViews(TestCase):

	def test_customer_list_Get(self):
		client = Client()
		response = client.get(reverse('list'))


		self.assertEquals(reponse.status_code,200)
		self.assertTemplateUsed(response, 'accounts/customer.html')




	
	def test_home(self):
		factory = RequestFactory()
		request = factory.get('/home/')
		response = home(request)
		self.assertEqual(200, response.status_code)


	def test_loginPage(self):
		factory = RequestFactory()
		request = factory.get('/login/')
		response = home(request)
		self.assertEqual(200, response.status_code)



	def test_acc_settings(self):
		factory = RequestFactory()
		request = factory.get('/account/')
		response = home(request)
		self.assertEqual(200, response.status_code)

	def test_user(self):
		factory = RequestFactory()
		request = factory.get('/user/')
		response = home(request)
		self.assertEqual(200, response.status_code)


	


