from ast import pattern
from django.urls import URLPattern,path
from . import views

urlpatterns = [
   path('temp_list',views.temp_list),
   path('temp_detail',views.temp_detail)
]


