from django.urls import URLPattern,path
from . import views

urlpatterns = [
   path('payment',views.Payment1,name='payment'),
   path('success/',views.success,name='success')
] 