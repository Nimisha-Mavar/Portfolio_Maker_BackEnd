from django.shortcuts import render

# Create your views here.
def temp_list(request):
    return render(request,'Template_list.html')

def temp_detail(request):
    return render(request,'Template_detail.html')

def premium_r_1(request):
    return render(request,'Premium_R_1.html')

def premium_r_2(request):
    return render(request,'Premium_R_2.html')

def premium_r_3(request):
    return render(request,'Premium_R_3.html')

