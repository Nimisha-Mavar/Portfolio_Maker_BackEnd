from django.contrib import admin
from django.contrib.admin.sites import site
from .models import contact,feedback
# Register your models here.
admin.site.register(contact)
admin.site.register(feedback)