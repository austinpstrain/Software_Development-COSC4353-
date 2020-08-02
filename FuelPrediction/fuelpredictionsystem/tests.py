
from django.test import TestCase
#from hypothesis.extra.django import TestCase
import pytest
from mixer.backend.django import mixer
from .models import *



class TestUserProfiletModel(TestCase):
     

         
    def test_add_a_plus_b(self):
        a = 1
        b = 2
        c = a + b

        assert c == 3


    def test_city(self):
        
        city1 = mixer.blend(UserProfile, city = "Houston" )
        city_result = UserProfile.objects.last()
        self.assertEqual(city_result.city, "Houston")

    def test_user(self):
        st1 = mixer.blend(UserProfile, state="Texas")
        st_result = UserProfile.objects.last()
        self.assertEqual(st_result.state, "Texas")


    def test_address(self):
        add1 = mixer.blend(UserProfile, address="Texas")
        add_result = UserProfile.objects.last()
        self.assertEqual(add_result.address, "Texas")

    def test_delivery(self):
        del1 = mixer.blend(PriceHistoryModule, delivery_address="Texas")
        add_result = PriceHistoryModule.objects.last()
        self.assertEqual(add_result.delivery_address, "Texas")





    

    