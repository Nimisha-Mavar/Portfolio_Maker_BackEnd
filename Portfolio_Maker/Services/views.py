from django.shortcuts import render

# Create your views here.
def edit(request):
    cat=request.POST['cat']
    if cat=="Portfolio":
        return render(request,'Portfolio_form.html')
    else:
        return render(request,'Resume_form.html')