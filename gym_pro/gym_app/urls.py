from django.contrib import admin
from django.urls import path
from gym_app import views
urlpatterns = [
    path('',views.Home,name="Home" ),
    path('signup',views.signup,name="signup" ),
    path('login',views.handlelogin,name="login" ),
    path('logout',views.logout_user,name="logout" ),




]