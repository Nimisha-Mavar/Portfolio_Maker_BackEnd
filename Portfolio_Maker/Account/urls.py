from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('login',views.login ,name="Login"),
    path('Register',views.Register, name="Register"),
    path('Logout',views.logout,name="Logout")
]