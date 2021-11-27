from django.db import models
# from course_registration_project.home.models import user

# Create your models here.


class course(models.Model):
    name=models.CharField(max_length=100)
    course_id=models.CharField(max_length=100,primary_key=True)
    days=models.TextField(null=True)
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)
    description=models.TextField(null=True)
    
class available_course(course):
    prof_name=models.CharField(max_length=100)
    prof_id=models.CharField(max_length=100)
    seats_available=models.IntegerField(default=0)
    prerequisites=models.TextField(null=True)
    



# primary key should be a compound key made of the combinarion of course_id and prerequisite_course_id, hence django will automatically create
class course_prerequsiteCourse(models.Model):
    course_id=models.ForeignKey(available_course, on_delete=models.CASCADE)
    prerequisite_course_id=models.CharField(max_length=100,null=True)



    