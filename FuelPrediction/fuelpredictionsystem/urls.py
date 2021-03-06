from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("home/", views.home, name='home'),
    path('clientRegistration/', views.register, name='clientRegistration'),
    path('clientProfile/', views.profile, name='clientProfile'),
    path('editProfile', views.editProfile, name='editProfile'),
    path('fqf/', views.fuelQuoteForm, name='fuelpredictionsystem-fqf'),
    path('fqh/', views.fuelQuoteHistory, name='fuelpredictionsystem-fqh'),
]