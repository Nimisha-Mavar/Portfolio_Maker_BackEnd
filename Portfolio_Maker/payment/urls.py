from django.urls import URLPattern,path
from . import views

urlpatterns = [
   #for ready template
   path('Ready',views.Ready_page,name="Ready"),
   #path('pay',views.payment,name='pay'),
   path('success/',views.success,name='success')
] 