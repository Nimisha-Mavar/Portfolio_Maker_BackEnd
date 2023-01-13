from django.shortcuts import render

# Create your views here.
def scanner_page(request):
    return render(request,'Scanner.html')