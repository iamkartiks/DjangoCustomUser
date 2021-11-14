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
    path('delete_address/<str:pk>',views.deleteAddress, name="address_delete"),
    path('delete_email/<str:pk>',views.deleteAddress, name="email_delete"),
    path('delete_username/<str:pk>',views.deleteAddress, name="username_delete"),
    path('delete_user/<str:pk>',views.deleteUser, name="user_delete"),
    path('logout/',views.logOut,name="logout")
]