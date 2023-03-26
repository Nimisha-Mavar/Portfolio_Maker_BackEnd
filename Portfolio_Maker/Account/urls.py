from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('login',views.login ,name="Login"),
    path('Register',views.Register, name="Register"),
    path('Logout',views.logout,name="Logout"),
    path('forgot_password',views.forgot_password,name="forgot_password"),
    path('set_pass', views.set_pass, name="set_pass"),
    path('change_pass',views.cng_pass,name="change_pass")
]