
from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('',views.home),
    path('faq',views.faq,name="faq"),
    path('contact1',views.contact1,name='contact1'),
    path('payment',views.payment1,name='payment')
]
