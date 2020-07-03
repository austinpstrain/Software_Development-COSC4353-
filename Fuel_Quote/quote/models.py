from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	Address_1 = models.CharField(max_length=200, null=True)
	Address_2 = models.CharField(max_length=200, null=True)
	City = models.CharField(max_length=200, null=True)
	State = models.CharField(max_length=200, null=True)
	Zip_Code = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name





	
