from django.contrib import admin
from .models import Favourite
from django.contrib.admin.sites import site
# Register your models here.
admin.site.register(Favourite)