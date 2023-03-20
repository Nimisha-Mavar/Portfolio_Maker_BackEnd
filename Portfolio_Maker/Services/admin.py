from django.contrib import admin
from django.contrib.admin.sites import site
from .models import *
# Register your models here.

admin.site.register(Personal_info),
admin.site.register(Education),
admin.site.register(Experience),
admin.site.register(Project),
admin.site.register(Skill),
admin.site.register(Award),
admin.site.register(Social_Media)
