from django.urls import path,URLPattern
from . import views

urlpatterns=[
    path('Edit',views.edit,name="Edit")
]