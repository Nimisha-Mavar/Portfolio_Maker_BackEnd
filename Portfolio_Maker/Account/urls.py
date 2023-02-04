from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('login',views.login),
    path('Register',views.register)
]