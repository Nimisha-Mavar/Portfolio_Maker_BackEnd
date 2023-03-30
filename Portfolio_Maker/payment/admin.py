from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Payment
# Register your models here.
admin.site.register(Payment)