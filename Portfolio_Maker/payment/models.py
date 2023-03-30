from django.db import models
from Templates.models import Detail
from Services.models import Resume,Portfolio

# Create your models here.
class Payment(models.Model):
    Resume=models.ForeignKey(Resume,null=True,on_delete=models.CASCADE)
    Portfolio=models.ForeignKey(Portfolio,null=True,on_delete=models.CASCADE)
    Temp_price = models.ForeignKey(Detail,null=True,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    razor_pay_order_id = models.CharField(max_length=100, null=True, blank=True)
