from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from pick_courses import views

urlpatterns = [
    path('pick_course',views.display_courses,name="display_courses"),
    path('add_course',views.add_courses,name="add_course"),
    path('update_course',views.update_course,name="update_course"),
    path('delete_course',views.delete_course,name="delete_course"),
    path('register_course',views.register_course,name="register_course"),
    path('unregister_course',views.unregister_course,name="unregister_course"),
    path('search',views.search,name="search"),
    path('navbar',views.disp_nav,name="disp_nav"),
]