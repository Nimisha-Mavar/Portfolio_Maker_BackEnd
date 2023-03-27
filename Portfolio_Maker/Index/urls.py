
from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('',views.home),
    path('faq',views.faq, name="faq"),
    path('contact1',views.contact1, name='contact1'),
    path('feedback/<int:id>',views.feed_page, name='feed'),
    path('feedback',views.feed, name='feedback'),
    path('',views.home,name="/"),
    path('faq',views.faq,name="faq"),
    path('contact1',views.contact1,name='contact1')
]
