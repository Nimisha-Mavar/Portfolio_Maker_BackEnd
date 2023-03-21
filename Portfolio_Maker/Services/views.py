from django.shortcuts import render,HttpResponse
from .models import Personal_info,Education

# Create your views here.
# Personal info function
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
            if Personal_info.objects.filter(Portfolio_id=port_id).exists():
                obj=Personal_info.objects.get(Portfolio_id=port_id)
                obj.First_name=fname
                obj.Last_name=lname
                obj.Address=address
                obj.Phone=phone
                obj.Email=eml
                obj.Dob=dob
                obj.Philosophy=philo
                obj.save()
                return HttpResponse('Data updated successfully')
            else:
                p_id=Personal_info.objects.only('Personal_id').count()
                p_id=p_id+1
                obj=Personal_info(Personal_id=p_id,Portfolio_id=port_id,First_name=fname,Last_name=lname,Address=address,Phone=phone,Email=eml,Dob=dob,Philosophy=philo)
                obj.save()
                return HttpResponse('Data stored successfully')
        else:
            print("is in else part")
            res_id=request.POST['res_id']
            p_id=Personal_info.objects.only('Personal_id').count()
            p_id=p_id+1
            data=Personal_info(Personal_id=p_id,Resume_id=res_id,First_name=fname,Last_name=lname,Address=address,Phone=phone,Email=eml,Dob=dob,Philosophy=philo)
            data.save()
            return HttpResponse('Data stored successfully')
    else:
        return HttpResponse('Error')

# Education function
def Education_data(request):
    if request.method == 'POST': 
        port_id=request.POST['port_id']
        cat=request.POST['catt']
        iname=request.POST['iname']
        degree=request.POST['degree']
        syear=request.POST['syear']
        eyear=request.POST['eyear']
        prsnt=request.POST['curnt']
        if cat=="Portfolio":
            eid=Education.objects.only('Education_id').count()
            eid=eid+1
            edu=Education.objects.filter(Portfolio_id=port_id)
            context={
                    'edu':edu
                }
            if prsnt == "True":
                obj=Education(Education_id=eid,Portfolio_id=port_id,Institute=iname,Degree=degree,Start_year=syear,Current=prsnt)
                obj.save()
                return HttpResponse("Data stored successfully...",context)
            else:
                obj=Education(Education_id=eid,Portfolio_id=port_id,Institute=iname,Degree=degree,Start_year=syear,End_year=eyear)
                obj.save()
                return HttpResponse("Data stored successfully...",context)
        else:
            return HttpResponse("Resume")
    else:
        return HttpResponse("Error")

def Education_del(request):
    if request.method == "POST":
        cat=request.POST['cat']
        Eu_id=request.POST['Euid']
        if cat=="Portfolio":
            obj=Education.objects.get(Education_id=Eu_id)
            obj.delete()
            return HttpResponse("Record deleted successfully")
        else:
            obj=Education.objects.get(Education_id=Eu_id)
            obj.delete()
            return HttpResponse("Record deleted successfully")