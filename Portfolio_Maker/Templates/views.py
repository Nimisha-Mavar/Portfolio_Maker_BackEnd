from django.shortcuts import render

# Create your views here.
def temp_list(request):
    return render(request,'Template_list.html')

def temp_detail(request):
    return render(request,'Template_detail.html')

