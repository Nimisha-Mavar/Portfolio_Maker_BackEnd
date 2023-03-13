from django.shortcuts import render

# Create your views here.
def edit(request):
    cat=request.POST['cat']
    if cat=="Portfolio":
        return render(request,'Edit_port.html')
    else:
        return render(request,'FAQ.html')