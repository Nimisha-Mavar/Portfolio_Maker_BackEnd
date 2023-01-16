from ast import pattern
from django.urls import URLPattern,path
from . import views

urlpatterns = [
   path('temp_list',views.temp_list),
   path('temp_detail',views.temp_detail),
   path('Basic_pf_1',views.Basic_pf_1),
   path('Basic_pf_2',views.Basic_pf_2),
   path('Premium_pf_1',views.Premium_pf_1),
   path('Premium_pf_2',views.Premium_pf_2),
   path('Premium_pf_3',views.Premium_pf_3),
]


