from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('login',views.login ,name="Login"),
    path('Register',views.Register, name="Register"),
    path('Logout',views.logout,name="Logout"),
    path('forgot_password',views.forgot_password,name="forgot_password"),
    path('forgot_pass1',views.forgot_pass1, name="forgot_pass1")
]