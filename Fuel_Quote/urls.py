from django.urls import path

from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('quote/', views.quote),
    path('history/', views.history),
    path('registerClient/', views.registerClient, name="registerClient"),
    path('profileManager/', views.profileManager),
    path('home/', views.home),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('customer/', views.customer),
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="quote/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="quote/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="quote/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="quote/password_reset_done.html"), 
        name="password_reset_complete"),



    ]