from django.shortcuts import render

# Create your views here.
def scanner_page(request):
    return render(request,'Scanner.html')

def keyword(request):
    return render(request,'Scan_Keyword.html')

def rate(request):
    return render(request,'Scan_Rate.html')