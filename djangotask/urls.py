from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.logIn, name="login"),
    path('signup/', views.signUp, name="signup"),
    path('userdetails/<str:pk>/',views.userDetails,name="details"),
    path('edit_email/',views.emailSettings, name="email_edit"),
    path('edit_username/',views.usernameSettings, name="username_edit"),
    path('edit_address/',views.addressSettings, name="address_edit"),
    path('logout/',views.logOut,name="logout")
]