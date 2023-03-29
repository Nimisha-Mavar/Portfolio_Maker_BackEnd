from django.db import models
from Templates.models import Detail
from django.contrib.auth.models import User, auth
# Create your models here.
#Portfolio model
class Portfolio(models.Model):
    Portfolio_id=models.IntegerField(primary_key=True)
    Template=models.ForeignKey(Detail,default=0,on_delete=models.CASCADE)
    User=models.ForeignKey(User,default=0,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Portfolio_id)
    def temp_nm(self):
        return self.Template.Temp_name
    def temp_cat(self):
        return self.Template.Temp_cat
    def temp_img(self):
        return self.Template.Temp_img1
    def temp_type(self):
        return self.Template.Temp_type
    def temp_prc(self):
        return self.Template.Temp_price
#Resume model
class Resume(models.Model):
    Resume_id=models.IntegerField(primary_key=True)
    Template=models.ForeignKey(Detail,default=0,on_delete=models.CASCADE)
    User=models.ForeignKey(User,default=0,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.Resume_id)
    def temp_nm(self):
        return self.Template.Temp_name
    def temp_cat(self):
        return self.Template.Temp_cat
    def temp_img(self):
        return self.Template.Temp_img1

#Personal Information
class Personal_info(models.Model):
    Personal_id=models.IntegerField(primary_key=True)
    First_name=models.CharField(max_length=30)
    Last_name=models.CharField(max_length=30)
    Address=models.TextField()
    Phone=models.CharField(max_length=10)
    Email=models.EmailField()
    Dob=models.DateField()
    Philosophy=models.TextField()
    Pic=models.ImageField(upload_to='Personal_Pic',null=True,blank=True)
    User=models.ForeignKey(User,default=0,on_delete=models.CASCADE)

#educaion model
class Education(models.Model):
    Education_id=models.IntegerField(primary_key=True)
    Resume=models.ForeignKey(Resume,null=True,on_delete=models.CASCADE)
    Portfolio=models.ForeignKey(Portfolio,null=True,on_delete=models.CASCADE)
    Institute=models.CharField(max_length=50)
    Degree=models.CharField(max_length=50)
    Start_year=models.CharField(max_length=10)
    End_year=models.CharField(max_length=10,null=True)
    Current=models.BooleanField(default=False)

#Experience model
class Experience(models.Model):
    Experience_id=models.IntegerField(primary_key=True)
    Resume=models.ForeignKey(Resume,null=True,on_delete=models.CASCADE)
    Portfolio=models.ForeignKey(Portfolio,null=True,on_delete=models.CASCADE)
    Company=models.CharField(max_length=50)
    Role=models.CharField(max_length=30)
    Start_year=models.CharField(max_length=10)
    End_year=models.CharField(max_length=10,null=True)
    Current=models.BooleanField(default=False)
    Description=models.TextField(null=True)

#Project model
class Project(models.Model):
    Project_id=models.IntegerField(primary_key=True)
    Resume=models.ForeignKey(Resume,null=True,on_delete=models.CASCADE)
    Portfolio=models.ForeignKey(Portfolio,null=True,on_delete=models.CASCADE)
    Title=models.CharField(max_length=50)
    Start_year=models.CharField(max_length=10)
    End_year=models.CharField(max_length=10,null=True)
    Current=models.BooleanField(default=False)
    Description=models.TextField(null=True)

#Skill model
class Skill(models.Model):
    Skill_id=models.IntegerField(primary_key=True)
    Resume=models.ForeignKey(Resume,null=True,on_delete=models.CASCADE)
    Portfolio=models.ForeignKey(Portfolio,null=True,on_delete=models.CASCADE)
    Name=models.CharField(max_length=30)
    Level=models.CharField(max_length=20)

#Award model
class Award(models.Model):
    Award_id=models.IntegerField(primary_key=True)
    Portfolio=models.ForeignKey(Portfolio,default=0,on_delete=models.CASCADE)
    Title=models.CharField(max_length=50)
    Institute=models.CharField(max_length=50)
    Year=models.CharField(max_length=10)
    Description=models.TextField(null=True)

class Social_Media(models.Model):
    Social_id=models.IntegerField(primary_key=True)
    Portfolio=models.ForeignKey(Portfolio,default=0,on_delete=models.CASCADE)
    Name=models.CharField(max_length=50)
    Url=models.TextField()




