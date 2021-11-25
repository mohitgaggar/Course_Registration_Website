from django.contrib import admin
from django.contrib import admin
# Register your models here.

from pick_courses.models import course,available_course

admin.site.register(course)
admin.site.register(available_course)