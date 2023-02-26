from django.urls import path,URLPattern
from . import views

urlpatterns=[
    path('Dashboard',views.dashboard,name='Dashboard')
]