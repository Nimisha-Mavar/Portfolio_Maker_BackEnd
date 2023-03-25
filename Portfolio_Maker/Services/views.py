from django.shortcuts import render,HttpResponse
from .models import Personal_info,Education,Experience,Project,Skill,Award,Social_Media

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
        if cat=="Portfolio":
            if Education.objects.filter(Portfolio_id=port_id,Institute=iname,Degree=degree).exists():
                return HttpResponse("Record exist....")
            else:
                eid=Education.objects.only('Education_id').count()
                eid=eid+1
                obj=Education(Education_id=eid,Portfolio_id=port_id,Institute=iname,Degree=degree,Start_year=syear,End_year=eyear)
                obj.save()
                return HttpResponse("Data stored successfully...")
        else:
            res_id=request.POST['res_id']
            eid=Education.objects.only('Education_id').count()
            eid=eid+1
            obj=Education(Education_id=eid,Resume_id=res_id,Institute=iname,Degree=degree,Start_year=syear,End_year=eyear)
            obj.save()
            return HttpResponse("Data stored successfully...")
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

#foe experience
def Experience_data(request):
    if request.method == 'POST': 
        port_id=request.POST['port_id']
        cat=request.POST['catt']
        cname=request.POST['cname']
        rname=request.POST['rname']
        syear=request.POST['syear']
        eyear=request.POST['eyear']
        des=request.POST['des']
        if cat=="Portfolio":
            if Experience.objects.filter(Portfolio_id=port_id,Company=cname,Role=rname).exists():
               return HttpResponse("Record Exist...")
            else:
                eid=Experience.objects.only('Experience_id').count()
                eid=eid+1
                obj=Experience(Experience_id=eid,Portfolio_id=port_id,Company=cname,Role=rname,Start_year=syear,End_year=eyear,Description=des)
                obj.save()
                return HttpResponse("Data stored successfully...")
        else:
            res_id=request.POST['res_id']
            eid=Experience.objects.only('Experience_id').count()
            eid=eid+1
            obj=Experience(Experience_id=eid,Resume_id=res_id,Company=cname,Role=rname,Start_year=syear,End_year=eyear,Description=des)
            obj.save()
            return HttpResponse("Data stored successfully...")
    else:
        return HttpResponse("Error")

#for Project
def Project_data(request):
    if request.method == 'POST': 
        cat=request.POST['catt']
        title=request.POST['title']
        curnt=request.POST['curnt']
        syear=request.POST['syear']
        eyear=request.POST['eyear']
        des=request.POST['des']
        print(curnt)
        if cat=="Portfolio":
            port_id=request.POST['port_id']
            if Project.objects.filter(Portfolio_id=port_id,Title=title).exists():
               return HttpResponse("Record Exist...")
            else:
                pid=Project.objects.only('Project_id').count()
                pid=pid+1
                if curnt=="yes":
                    curnt=True
                else:
                    curnt=False
                obj=Project(Project_id=pid,Portfolio_id=port_id,Title=title,Start_year=syear,End_year=eyear,Description=des,Current=curnt)
                obj.save()
                return HttpResponse("Data stored successfully...")
        else:
            res_id=request.POST['res_id']
            pid=Project.objects.only('Project_id').count()
            pid=pid+1
            obj=Project(Project_id=pid,Resume_id=res_id,Title=title,Start_year=syear,End_year=eyear,Description=des,Current=curnt)
            obj.save()
            return HttpResponse("Data stored successfully...")
    else:
        return HttpResponse("GET method called...")
    
def Skill_data(request):
    if request.method == 'POST':
        cat=request.POST['catt']
        sname=request.POST['sk_nm']
        lvl=request.POST['lvl']
        if cat=="Portfolio":
           port_id=request.POST['port_id']
           if Skill.objects.filter(Portfolio_id=port_id,Name=sname).exists():
               return HttpResponse("Record Exist...")
           else:
                sid=Skill.objects.only('Skill_id').count()
                sid=sid+1 
                obj=Skill(Skill_id=sid,Portfolio_id=port_id,Name=sname,Level=lvl)
                obj.save()
                return HttpResponse("Data stored successfully...")
        else:
            return HttpResponse("Resumee")
    else:
       return HttpResponse("GET method called...")

def Award_data(request):
    if request.method == 'POST':
        port_id=request.POST['port_id']
        title=request.POST['ttl']
        institute=request.POST['ints']
        year=request.POST['year']
        des=request.POST['des']
        if Award.objects.filter(Portfolio_id=port_id,Title=title,Institute=institute).exists():
            return HttpResponse("Record Exist...")
        else:
            aid=Award.objects.only('Award_id').count()
            aid=aid+1 
            obj=Award(Award_id=aid,Portfolio_id=port_id,Title=title,Institute=institute,Year=year,Description=des)
            obj.save()
            return HttpResponse("Data stored successfully...")
    else:
       return HttpResponse("GET method called...")  
    
def Social_data(request):
    if request.method == 'POST':
        act=request.POST['snm']
        url=request.POST['url']
        port_id=request.POST['port_id']
        if Social_Media.objects.filter(Portfolio_id=port_id,Name=act).exists():
            return HttpResponse("Record Exist...")
        else:
            sid=Social_Media.objects.only('Social_id').count()
            sid=sid+1 
            obj=Social_Media(Social_id=sid,Portfolio_id=port_id,Name=act,Url=url)
            obj.save()
            return HttpResponse("Data stored successfully...")
    else:
       return HttpResponse("GET method called...")