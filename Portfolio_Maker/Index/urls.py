from ast import pattern
from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('',views.home)
]
