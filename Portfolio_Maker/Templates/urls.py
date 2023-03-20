
from django.urls import URLPattern,path
from . import views

urlpatterns = [
   path('Resume-list',views.Resume_list,name="Resume-list"),
   path('Portfolio-list',views.Portfolio_list,name="Portfolio-list"),
   path('ATS-list',views.ATS_list,name="ATS-list"),
   path('<int:id>',views.temp_detail),
   path('Form',views.form),
   path('select_delete',views.select_dlt,name="select_delete"),
   path('Edit',views.edit,name="Edit"),
]


