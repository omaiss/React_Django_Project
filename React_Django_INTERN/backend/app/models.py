from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    otp=models.CharField(max_length=6, null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    
# position, name , email, job, department
# job scheduling
# background scheduling

class Custom_User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    