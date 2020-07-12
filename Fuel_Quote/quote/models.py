from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):

    CATEGORY = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansan'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),

    )
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    Address_1 = models.CharField(max_length=100, null=True)
    Address_2 = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=100, null=True)
    State = models.CharField(max_length=100, null=True, choices=CATEGORY)
    Zip_Code = models.CharField(max_length=10, null=True)
    profile_pic = models.ImageField(
        default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    user = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    gallons_requested = models.FloatField(null=True)
    Address_1 = models.CharField(max_length=100, null=True)
    Address_2 = models.CharField(max_length=100, null=True)
    delivery_date = models.DateField(null=True)
    name = models.CharField(max_length=50, null=True)
    suggested_price = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Pricing(models.Model):
    gallons_requested = models.ForeignKey(
        Getquote, null=True, on_delete=models.SET_NULL)
    suggested_price = models.FloatField(null=True)
    customer = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL)

    def __float__(self):
        return self.suggested_price
