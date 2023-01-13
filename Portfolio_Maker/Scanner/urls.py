from ast import pattern
from django.urls import URLPattern,path
from . import views

urlpatterns = [
    path('scanner',views.scanner_page),
    path('scan_keyword',views.keyword)
]