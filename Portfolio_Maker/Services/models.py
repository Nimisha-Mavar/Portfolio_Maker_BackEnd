from django.db import models
from Templates.models import Detail
from django.contrib.auth.models import User, auth
# Create your models here.
#Portfolio model
class Portfolio(models.Model):
    Portfolio_id=models.IntegerField(primary_key=True)
    Template=models.ForeignKey(Detail,default=0,on_delete=models.CASCADE)
    User=models.ForeignKey(User,default=0,on_delete=models.CASCADE)

#Resume model
class Resume(models.Model):
    Resume_id=models.IntegerField(primary_key=True)
    Template=models.ForeignKey(Detail,default=0,on_delete=models.CASCADE)
    User=models.ForeignKey(User,default=0,on_delete=models.CASCADE)

#Personal Information
class Personal_info(models.Model):
    Personal_id=models.IntegerField(primary_key=True)
    Resume=models.ForeignKey(Resume,default=0,on_delete=models.CASCADE)
    Portfolio=models.ForeignKey(Portfolio,default=0,on_delete=models.CASCADE)
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    Address=models.TextField()
    Phone=models.CharField(max_length=10)
    Email=models.EmailField()
    Dob=models.DateField()
    Philosophy=models.TextField()

#educaion model
class Education(models.Model):
    Education_id=models.IntegerField(primary_key=True)
    Resume=models.ForeignKey(Resume,default=0,on_delete=models.CASCADE)
    Portfolio=models.ForeignKey(Portfolio,default=0,on_delete=models.CASCADE)
    Institute=models.CharField(max_length=50)
    Degree=models.CharField(max_length=50)
    Start_year=models.CharField(max_length=10)
    End_year=models.CharField(max_length=10,default='no')
    Current=models.BooleanField(default=False)

#Experience model
class Experience(models.Model):
    Experience_id=models.IntegerField(primary_key=True)
    Resume=models.ForeignKey(Resume,default=0,on_delete=models.CASCADE)
    Portfolio=models.ForeignKey(Portfolio,default=0,on_delete=models.CASCADE)
    Company=models.CharField(max_length=50)
    Role=models.CharField(max_length=30)
    Start_year=models.CharField(max_length=10)
    End_year=models.CharField(max_length=10,default='no')
    Current=models.BooleanField(default=False)

#Project model
class Project(models.Model):
    Project_id=models.IntegerField(primary_key=True)
    Resume=models.ForeignKey(Resume,default=0,on_delete=models.CASCADE)
    Portfolio=models.ForeignKey(Portfolio,default=0,on_delete=models.CASCADE)
    Title=models.CharField(max_length=50)
    Start_year=models.CharField(max_length=10)
    End_year=models.CharField(max_length=10,default='no')
    Current=models.BooleanField(default=False)
    Description=models.TextField(default="NO")

#Skill model
class Skill(models.Model):
    Skill_id=models.IntegerField(primary_key=True)
    Resume=models.ForeignKey(Resume,default=0,on_delete=models.CASCADE)
    Portfolio=models.ForeignKey(Portfolio,default=0,on_delete=models.CASCADE)
    Name=models.CharField(max_length=30)
    Level=models.CharField(max_length=20)



