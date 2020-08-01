from django.test import TestCase

# Create your tests here.

class TestUserProfile(TestCase):

	def test_add(self):
		a = 1
		b=2

		c = a+b


		self.assertEqual(c,3)
