from django.urls import URLPattern,path
from . import views

urlpatterns = [
# Portfolio Templates
   path('MyPortfolio',views.Basic_pf_1,name="MyPortfolio"),
   path('RightFolio',views.Basic_pf_2,name="RightFolio"),
   path('Persnal',views.Premium_pf_1,name="Persnal"),
   path('Laura',views.Premium_pf_2,name="Laura"),
   path('iportfolio',views.Premium_pf_3,name="iportfolio"),
# Resume Templates
   path('YellowResume',views.Basic_Rm_1,name="YelloResume"),
   path('GreyResume',views.Basic_Rm_2,name="GreyResume"),
   path('BlueAndGrey',views.Premium_Rm_1,name="BlueAndGrey"),
   path('BlueResume',views.Premium_Rm_2,name="BlueResume")
]