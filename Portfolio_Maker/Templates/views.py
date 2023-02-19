from django.shortcuts import render
from .models import Detail
# Create your views here.
def Resume_list(request):
    temp="Resume"
    resume=Detail.objects.filter(Temp_cat=temp)
    return render(request,'Template_list.html',{'Temps':resume})

def Portfolio_list(request):
    temp="Portfolio"
    Ports=Detail.objects.filter(Temp_cat=temp)
    return render(request,'Template_list.html',{'Temps':Ports})

def ATS_list(request):
    temp="ATS"
    ATS=Detail.objects.filter(Temp_cat=temp)
    return render(request,'Template_list.html',{'Temps':ATS})

def temp_detail(request):
    return render(request,'Template_detail.html')

