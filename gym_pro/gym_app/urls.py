from django.contrib import admin
from django.urls import path
from gym_app import views
urlpatterns = [
    path('',views.Home,name="Home" ),
    path('signup',views.signup,name="signup" ),
    path('login',views.handlelogin,name="login" ),
    path('logout',views.logout_user,name="logout" ),
    path('contact',views.contact,name="contact" ),
    path('join',views.handleEnroll,name="handleEnroll" ),
    path('profile',views.handleprofile,name="handleprofile" ),
    path('gallary',views.handle_gallary,name="handle_gallary" ),
    path('attendance',views.handle_att,name="handle_att" ),









]