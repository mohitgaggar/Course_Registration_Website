from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('signin',views.signin_user,name="signin"),
    path('signup',views.signup_user,name="singup"),
    path('signout',views.signout_user,name="singout"),
    

]