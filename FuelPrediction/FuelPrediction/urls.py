"""FuelPrediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from fuelpredictionsystem import views as v
#from . import views

urlpatterns = [
	#path('', include('main.urls')), # main will be the name of your app
	path('admin/', admin.site.urls),
	path('', include('fuelpredictionsystem.urls')),
	# path('clientProfile/', include('fuelpredictionsystem.urls')),
	# path('fqf/', include('fuelpredictionsystem.urls')),
	# path('fqh/', include('fuelpredictionsystem.urls')),
	path("clientRegistration/", v.register, name="clientRegistration"),
	# path("clientProfile/", v.clientProfile, name="clientProfile"),
	path("clientProfile/", v.profile, name="clientProfile"),
	path('fqf/', v.fuelQuoteForm, name="fuelQuoteForm"),
	path('fqh/', v.fuelQuoteHistory, name="fuelQuoteHistory"),
	path('', include("django.contrib.auth.urls")),
	#path("clientRegistration/", include('fuelpredictionsystem.urls')),
	path("loginHome/", v.loginHome, name="Home"),
	path("editProfile/", v.editProfile, name="editProfile"),
	path('success/', include('fuelpredictionsystem.urls')),
]