from django.db import models

class myuser(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    user_id=models.CharField(max_length=100,primary_key=True)
    courses_taken=models.TextField(null=True)  # will store list of course objects as a textfield
    registered_courses=models.TextField(null=True)  
    