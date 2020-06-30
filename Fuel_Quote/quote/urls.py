from django.urls import path
from . import views

urlpatterns = [
    path('quote/', views.quote),
    path('history/', views.history),
    path('registerClient/', views.registerClient),
    path('profileManager/', views.profileManager),
    path('home/', views.home),
    path('login/', views.login),
    path('', views.home)
]