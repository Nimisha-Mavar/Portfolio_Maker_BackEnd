from django.urls import path,URLPattern
from . import views

urlpatterns=[
    path('Personal_data',views.Personal,name="Personal_data")
]