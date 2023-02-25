from django.db import models
from Templates.models import Detail
from django.contrib.auth.models import User, auth
# Create your models here.
#Portfolio model
class Portfolio(models.Model):
    Portfolio_id=models.IntegerField(primary_key=True)
    Template=models.ForeignKey(Detail,default=0,on_delete=models.CASCADE)
    User=models.ForeignKey(User,default=0,on_delete=models.CASCADE)
