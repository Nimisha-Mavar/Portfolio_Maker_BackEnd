from django.urls import path,URLPattern
from . import views

urlpatterns=[
    path('Personal_data',views.Personal,name="Personal_data"),
    path('Education_data',views.Education_data,name="Education_data"),
    path('Education_del',views.Education_del,name="Education_del"),
    path('Experience_data',views.Experience_data,name="Experience_data"),
]