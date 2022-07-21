import email
from django.db import models
import datetime

# Create your models here.

dt = datetime.datetime.now()

class questions(models.Model):
    email = models.CharField(max_length=50)
    userName = models.CharField(max_length=30)
    mobileNum = models.CharField(max_length=12)
    question = models.CharField(max_length=200)
    date = models.DateTimeField(default=dt,blank=True)

class project(models.Model):
    project_name = models.CharField(max_length=50)
    project_link = models.URLField()
    project_dp = models.ImageField()
    project_description = models.CharField(max_length=70)
