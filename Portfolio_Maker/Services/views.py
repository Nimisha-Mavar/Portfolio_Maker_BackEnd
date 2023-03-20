from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def edit(request):
    cat=request.POST['cat']
    pid=request.POST['port_id']
    if cat=="Portfolio":
        return render(request,'Portfolio_form.html',{'portid':pid})
    else:
        return render(request,'Resume_form.html')
    
def Personal(request):
    if request.method == 'POST':
        fname=request.POST['fnm']
        lname=request.POST['lnm']
        address=request.POST['adr']
        phone=request.POST['phn']
        eml=request.POST['eml']
        dob=request.POST['dob']
        philo=request.POST['philo']
        port_id=request.POST['port_id']
        cat=request.POST['catt']
        print(cat)
        if cat=="Portfolio":
            p_id=Personal_info.objects.only('Personal_id').count()
            p_id=p_id+1
            print("iinnnnnnnnnn")
            obj=Personal_info(Personal_id=p_id,Portfolio_id=port_id,First_name=fname,Last_name=lname,Address=address,Phone=phone,Email=eml,Dob=dob,Philosophy=philo)
            obj.save()
            return HttpResponse('Data stored successfully')
        else:
            print("is in else part")
            res_id=request.POST['res_id']
            p_id=Personal_info.objects.only('Personal_id').count()
            p_id=p_id+1
            data=Personal_info(Personal_id=p_id,Resume=res_id,First_name=fname,Last_name=lname,Address=address,Phone=phone,Email=eml,Dob=dob,Philosophy=philo)
            data.save()
            return HttpResponse('Data stored successfully')
    else:
        return HttpResponse('Error')
        
