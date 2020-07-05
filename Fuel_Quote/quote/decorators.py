from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		#customer = Customer.objects.get(id = )
		if request.user.is_authenticated:
			return redirect('home',  1 )
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func



