from django.contrib import admin
from django.urls import path
from gym_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="Home" ),

]