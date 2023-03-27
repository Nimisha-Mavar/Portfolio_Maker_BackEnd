from django.db import models
from Templates.models import Detail
from django.contrib.auth.models import User, auth

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.TextField()
    message = models.TextField()
    
class feedback(models.Model):
    Rate1 = models.IntegerField(default=0)
    Message1 = models.TextField(max_length=200)
    Date1 = models.DateField(auto_now_add=True)
    Template=models.ForeignKey(Detail,null=True,on_delete=models.CASCADE)
    User=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)