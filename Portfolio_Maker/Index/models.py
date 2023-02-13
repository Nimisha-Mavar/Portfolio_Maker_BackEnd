from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.TextField()
    message = models.TextField()