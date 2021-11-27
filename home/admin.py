from django.contrib import admin

# Register your models here.
from home.models import myuser,user_registeredCourse,user_completedCourse

admin.site.register(myuser)
admin.site.register(user_registeredCourse)
admin.site.register(user_completedCourse)