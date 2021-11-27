from django.db import models

from pick_courses.models import available_course, course

class myuser(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    user_id=models.CharField(max_length=100,primary_key=True)
    courses_taken=models.TextField(null=True)  # will store list of course objects as a textfield
    registered_courses=models.TextField(null=True)  

# primary key should be a compound key made of the combinarion of user_id and course_id, hence django will automatically create
class user_registeredCourse(models.Model):
    user_id=models.ForeignKey(myuser, on_delete=models.CASCADE)
    course_id=models.ForeignKey(available_course, on_delete=models.CASCADE)

class user_completedCourse(models.Model):
    user_id=models.ForeignKey(myuser, on_delete=models.CASCADE)
    completed_course_id=models.CharField(max_length=100,null=True)


    