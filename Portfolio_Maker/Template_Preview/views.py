from django.shortcuts import render

# Portfolio Templates
def Basic_pf_1(request):
    return render(request,'Basic_Pf_1.html')

def Basic_pf_2(request):
    return render(request,'Basic_Pf_2.html')

def Premium_pf_1(request):
    return render(request,'Premium_Pf_1.html')

def Premium_pf_2(request):
    return render(request,'Premium_Pf_2.html')

def Premium_pf_3(request):
    return render(request,'Premium_Pf_3.html')

# Resume Template
def Basic_Rm_1(request):
    return render(request,'Basic_Resune_1.html')

def Basic_Rm_2(request):
    return render(request,'Premium_R_2.html')

def Premium_Rm_1(request):
    return render(request,'Premium_R_1.html')

def Premium_Rm_2(request):
    return render(request,'Premium_R_3.html')