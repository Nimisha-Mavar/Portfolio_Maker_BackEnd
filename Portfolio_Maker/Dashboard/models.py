from django.db import models
from Templates.models import Detail
from django.contrib.auth.models import User, auth

# Create your models here.
class Favourite(models.Model):
    Template=models.ForeignKey(Detail,default=0,on_delete=models.CASCADE)
    User=models.ForeignKey(User,default=0,on_delete=models.CASCADE)
    def img(self):
        return self.Template.Temp_img1
    def name(self):
        return self.Template.Temp_name
    def cat(self):
        return self.Template.Temp_cat