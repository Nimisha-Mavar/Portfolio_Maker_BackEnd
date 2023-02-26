from django.contrib import admin
from .models import Offer,Detail
from django.contrib.admin.sites import site
from Services.models import Portfolio,Resume
# Register your models here.
admin.site.register(Offer),
admin.site.register(Detail),
admin.site.register(Portfolio),
admin.site.register(Resume)