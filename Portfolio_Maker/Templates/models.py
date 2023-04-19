from django.db import models

class Offer(models.Model):
    Offer_id=models.IntegerField(primary_key=True)
    Offer=models.BooleanField(default=False)
    Offer_value=models.IntegerField()
    Start_date=models.DateField()
    End_date=models.DateField()
    

# Create your models here.
class Detail(models.Model):
    Temp_Cat=(
        ('Portfolio','Portfolio'),
        ('Resume','Resume'),
        ('ATS','ATS')
    )
    Temp_Type=(
        ('Basic','Basic'),
        ('Premium','Premium')
    )
    Temp_name=models.CharField(max_length=100)
    Temp_cat=models.CharField(max_length=30,default="Portfolio",choices=Temp_Cat)
    Temp_type=models.CharField(max_length=30,default="Basic",choices=Temp_Type)
    Temp_date=models.DateField()
    Temp_img1=models.ImageField(upload_to='Temp_Imgs')
    Temp_img2=models.ImageField(upload_to='Temp_Imgs',null=True)
    Temp_img3=models.ImageField(upload_to='Temp_Imgs',null=True)
    Temp_des=models.TextField()
    Temp_price=models.IntegerField()
    Temp_file=models.FileField(upload_to='Template_files')
    Temp_active=models.BooleanField(default=False)
    Temp_offer=models.ForeignKey('Offer',default=0,on_delete=models.SET_DEFAULT)
    def __str__(self):
        return self.Temp_name
    def offer(self):
        return self.Temp_offer.Offer_value
    

    