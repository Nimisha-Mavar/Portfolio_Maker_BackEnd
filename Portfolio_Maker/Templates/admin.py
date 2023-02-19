from django.contrib import admin
from .models import Offer,Detail
from django.contrib.admin.sites import site
# Register your models here.
admin.site.register(Offer),
admin.site.register(Detail)