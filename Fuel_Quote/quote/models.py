from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Quote(models.Model):
	sugestedPrice = models.FloatField()
	address = models.CharField(max_length = 200, null = True)
	deliveryDate = models.DateField()
	gallonsRequested = models.FloatField()
	Total = models.FloatField()

<<<<<<< HEAD
"""#class History(models.Model):
	#quote = """
=======
class Quote(models.Model):
	customer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
	gallons_requested = models.FloatField(null = True)
	Address_1 = models.CharField(max_length=100, null=True)
	Address_2 = models.CharField(max_length=100, null=True)
	delivery_date = models.DateField(null = True)
	suggested_price = models.FloatField(null = True)
	total_amount = models.FloatField(null = True)

	def __float__(self):
		return self.gallons_requested


	
>>>>>>> 3d93e5142f48af0fc36707fc7d7cfb3e313bd70d
