from django.urls import URLPattern,path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',views.login ,name="Login"),
    path('Register',views.Register, name="Register"),
    path('Logout',views.logout,name="Logout"),
    path('forgot_password',views.forgot_password,name="forgot_password"),
    path('set_pass', views.set_pass, name="set_pass"),
    path('change_pass',views.cng_pass,name="change_pass"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete",)

]