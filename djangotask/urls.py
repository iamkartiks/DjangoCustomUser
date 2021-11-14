from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.logIn, name="login"),
    path('signup/', views.signUp, name="signup"),
    path('userdetails/',views.userDetails,name="details")
]