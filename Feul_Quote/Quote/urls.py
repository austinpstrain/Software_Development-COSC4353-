from django.urls import path

from .import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('quote/', views.quote, name="quote"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('updateRequest/<str:pk>/', views.quote_form, name="quote_form"),
]
