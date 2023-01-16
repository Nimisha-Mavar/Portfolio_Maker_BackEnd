from django.shortcuts import render

# Create your views here.
def temp_list(request):
    return render(request,'Template_list.html')

def temp_detail(request):
    return render(request,'Template_detail.html')

def Basic_pf_1(request):
    return render(request,'Basic_Pf_1.html')

