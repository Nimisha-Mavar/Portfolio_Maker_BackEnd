
from django.urls import URLPattern,path
from . import views

urlpatterns = [
   path('temp_list',views.temp_list),
   path('temp_detail',views.temp_detail),
   path('premium_r_1',views.premium_r_1),
   path('premium_r_2',views.premium_r_2),
   path('premium_r_3',views.premium_r_3),
   path('basic_resume_1',views.basic_resume_1),
]


