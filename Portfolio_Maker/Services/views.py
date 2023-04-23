from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.http import HttpResponseRedirect

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
        cnty=request.POST.get('cnty')
        st=request.POST.get('st')
        cty=request.POST.get('cty')
        U_id=request.user
        if len(request.POST['pic']) != 0:
            pic=request.POST['pic']
        else:
            pic=''
        if Personal_info.objects.filter(User_id=U_id.id).exists():
                obj=Personal_info.objects.get(User_id=U_id.id)
                obj.First_name=fname
                obj.Last_name=lname
                obj.Address=address
                obj.Phone=phone
                obj.Email=eml
                obj.Dob=dob
                obj.Philosophy=philo
                obj.Pic=pic
                obj.Country=cnty
                obj.State=st
                obj.City=cty
                obj.save()
                return HttpResponse('Data updated successfully')
        else:
                p_id=Personal_info.objects.only('Personal_id').count()
                if p_id == 0:
                    p_id=1
                else:
                    p_id=(Personal_info.objects.last()).Personal_id
                    p_id+=1
                obj=Personal_info(Personal_id=p_id,User_id=U_id.id,First_name=fname,Last_name=lname,Address=address,Phone=phone,Email=eml,Dob=dob,Philosophy=philo,Pic=pic,Country=cnty,State=st,City=cty)
                obj.save()
                return HttpResponse('Data stored successfully')
    else:
        return HttpResponse('Error')

# Education function
def Education_data(request):
    if request.method == 'POST': 
        cat=request.POST['cat']
        iname=request.POST['iname']
        degree=request.POST['degree']
        syear=request.POST['syear']
        eyear=request.POST['eyear']
        des=request.POST.get('des')
        cunt=request.POST.get('crnt')
        if cunt=="yes":
            cunt=True
        else:
            cunt=False
        if cat=="Portfolio":
            port_id=request.POST['port_id']
            if Education.objects.filter(Portfolio_id=port_id,Institute=iname,Degree=degree).exists():
                return HttpResponse("Record exist....")
            else:
                eid=Education.objects.only('Education_id').count()
                if eid == 0:
                    eid=1
                else:
                    eid=(Education.objects.last()).Education_id
                    eid+=1
                obj=Education(Education_id=eid,Portfolio_id=port_id,Institute=iname,Degree=degree,Start_year=syear,End_year=eyear,Description=des,Current=cunt)
                obj.save()
                return HttpResponse("Data stored successfully...")
        else:
            res_id=request.POST['res_id']
            if Education.objects.filter(Resume_id=res_id,Institute=iname,Degree=degree).exists():
                return HttpResponse("Record exist....")
            else:
                eid=Education.objects.only('Education_id').count()
                if eid == 0:
                    eid=1
                else:
                    eid=(Education.objects.last()).Education_id
                    eid+=1
                obj=Education(Education_id=eid,Resume_id=res_id,Institute=iname,Degree=degree,Start_year=syear,End_year=eyear,Current=cunt,Description=des)
                obj.save()
                return HttpResponse("Data stored successfully...")
    else:
        return HttpResponse("Error")

def Education_del(request,id):
    obj=Education.objects.get(Education_id=id)
    obj.delete()
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

#foe experience
def Experience_data(request):
    if request.method == 'POST': 
        idd=request.POST['idd']
        cat=request.POST['cat']
        cname=request.POST['cname']
        rname=request.POST['rname']
        syear=request.POST['syear']
        eyear=request.POST['eyear']
        des=request.POST['des']
        cunt=request.POST.get('crnt')
        if cunt=="yes":
            cunt=True
        else:
            cunt=False
        if cat=="Portfolio":
            if Experience.objects.filter(Portfolio_id=idd,Company=cname,Role=rname).exists():
               return HttpResponse("Record Exist...")
            else:
                eid=Experience.objects.only('Experience_id').count()
                if eid == 0:
                    eid=1
                else:
                    eid=(Experience.objects.last()).Experience_id
                    eid+=1
                obj=Experience(Experience_id=eid,Portfolio_id=idd,Company=cname,Role=rname,Start_year=syear,End_year=eyear,Description=des,Current=cunt)
                obj.save()
                return HttpResponse("Data stored successfully...")
        else:
            eid=Experience.objects.only('Experience_id').count()
            if Experience.objects.filter(Resume_id=idd,Company=cname,Role=rname).exists():
               return HttpResponse("Record Exist...")
            else:
                if eid == 0:
                    eid=1
                else:
                    eid=(Experience.objects.last()).Experience_id
                    eid+=1
                obj=Experience(Experience_id=eid,Resume_id=idd,Company=cname,Role=rname,Start_year=syear,End_year=eyear,Description=des,Current=cunt)
                obj.save()
                return HttpResponse("Data stored successfully...")
    else:
        return HttpResponse("Error")

def Experience_del(request):
        eid=request.POST['id']
        obj=Experience.objects.get(Experience_id=eid)
        obj.delete()
        return HttpResponse("")

#for Project
def Project_data(request):
    if request.method == 'POST': 
        idd=request.POST['idd']
        cat=request.POST['cat']
        title=request.POST['title']
        curnt=request.POST['curnt']
        syear=request.POST['syear']
        eyear=request.POST['eyear']
        des=request.POST['dess']
        if curnt=="yes":
            curnt=True
        else:
            curnt=False
        if cat=="Portfolio":
            if Project.objects.filter(Portfolio_id=idd,Title=title).exists():
               return HttpResponse("Record Exist...")
            else:
                pid=Project.objects.only('Project_id').count()
                if pid == 0:
                   pid=1
                else:
                    pid=(Project.objects.last()).Project_id
                    pid+=1
                obj=Project(Project_id=pid,Portfolio_id=idd,Title=title,Start_year=syear,End_year=eyear,Description=des,Current=curnt)
                obj.save()
                return HttpResponse("Data stored successfully...")
        else:
            if Project.objects.filter(Resume_id=idd,Title=title).exists():
               return HttpResponse("Record Exist...")
            else:
                pid=Project.objects.only('Project_id').count()
                if pid == 0:
                    pid=1
                else:
                    pid=(Project.objects.last()).Project_id
                    pid+=1
                obj=Project(Project_id=pid,Resume_id=idd,Title=title,Start_year=syear,End_year=eyear,Description=des,Current=curnt)
                obj.save()
                return HttpResponse("Data stored successfully...")
    else:
        return HttpResponse("GET method called...")

def Project_del(request):
        eid=request.POST['id']
        obj=Project.objects.get(Project_id=eid)
        obj.delete()
        return HttpResponse("")

#for Skill  
def Skill_data(request):
    if request.method == 'POST':
        idd=request.POST['idd']
        cat=request.POST['cat']
        sname=request.POST['sk_nm']
        lvl=request.POST['lvl']
        if cat=="Portfolio":
           if Skill.objects.filter(Portfolio_id=idd,Name=sname).exists():
               return HttpResponse("Record Exist...")
           else:
                sid=Skill.objects.only('Skill_id').count()
                if sid == 0:
                   sid=1
                else:
                    sid=(Skill.objects.last()).Skill_id
                    sid+=1
                obj=Skill(Skill_id=sid,Portfolio_id=idd,Name=sname,Level=lvl)
                obj.save()
                return HttpResponse("Data stored successfully...")
        else:
            if Skill.objects.filter(Resume_id=idd,Name=sname).exists():
               return HttpResponse("Record Exist...")
            else:
                sid=Skill.objects.only('Skill_id').count()
                if sid == 0:
                   sid=1
                else:
                    sid=(Skill.objects.last()).Skill_id
                    sid+=1
                obj=Skill(Skill_id=sid,Resume_id=idd,Name=sname,Level=lvl)
                obj.save()
                return HttpResponse("Data stored successfully...")
    else:
       return HttpResponse("GET method called...")

def Skill_del(request):
        eid=request.POST['id']
        obj=Skill.objects.get(Skill_id=eid)
        obj.delete()
        return HttpResponse("")

#for Award
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
            if aid == 0:
                aid=1
            else:
                aid=(Award.objects.last()).Award_id
                aid+=1 
            obj=Award(Award_id=aid,Portfolio_id=port_id,Title=title,Institute=institute,Year=year,Description=des)
            obj.save()
            return HttpResponse("Data stored successfully...")
    else:
       return HttpResponse("GET method called...")  
    
def Award_del(request):
    eid=request.POST['id']
    obj=Award.objects.get(Award_id=eid)
    obj.delete()
    return HttpResponse("")

#for Social_Media   
def Social_data(request):
    if request.method == 'POST':
        act=request.POST['snm']
        url=request.POST['url']
        port_id=request.POST['port_id']
        if Social_Media.objects.filter(Portfolio_id=port_id,Name=act).exists():
            return HttpResponse("Record Exist...")
        else:
            sid=Social_Media.objects.only('Social_id').count()
            if sid == 0:
                sid=1
            else:
                sid=(Social_Media.objects.last()).Social_id
                sid+=1  
            obj=Social_Media(Social_id=sid,Portfolio_id=port_id,Name=act,Url=url)
            obj.save()
            return HttpResponse("Data stored successfully...")
    else:
       return HttpResponse("GET method called...")
    
def Social_del(request):
    eid=request.POST['id']
    obj=Social_Media.objects.get(Social_id=eid)
    obj.delete()
    return HttpResponse("")

#for section display   
def Data_display(request):
    cat=request.POST['Ccat']
    idd=request.POST['id']
    u_id=request.user
    if cat=="Portfolio":
        prs=Personal_info.objects.filter(User_id=u_id.id)
        edu=Education.objects.filter(Portfolio_id=idd)
        ex=Experience.objects.filter(Portfolio_id=idd)
        proj=Project.objects.filter(Portfolio_id=idd)
        skill=Skill.objects.filter(Portfolio_id=idd)
        award=Award.objects.filter(Portfolio_id=idd)
        social=Social_Media.objects.filter(Portfolio_id=idd)
        contaxt={
            'idd':idd,
            'prs':prs,
            'edu':edu,
            'ex':ex,
            'pro':proj,
            'sk':skill,
            'awd':award,
            'scl':social,
            'cat':cat
        }
        return render(request,'Section_Details.html',contaxt)
    else:
        prs=Personal_info.objects.filter(User_id=u_id.id)
        edu=Education.objects.filter(Resume_id=idd)
        ex=Experience.objects.filter(Resume_id=idd)
        proj=Project.objects.filter(Resume_id=idd)
        skill=Skill.objects.filter(Resume_id=idd)
        contaxt={
            'idd':idd,
            'prs':prs,
            'edu':edu,
            'ex':ex,
            'pro':proj,
            'sk':skill,
            'active':True,
            'cat':cat
        }
        return render(request,'Section_Details.html',contaxt)
    
#for Url 
def Get_url(request):
    pid=request.POST['pid']
    pdata=Portfolio.objects.get(Portfolio_id=pid)
    tid=pdata.Template_id
    tname=pdata.temp_nm()
    tcat=pdata.temp_cat()
    ttype=pdata.temp_type()
    prc=pdata.temp_prc()
    url="http://127.0.0.1:8000/Livedemo/"+tname+"?pid="+pid
    Data={
        'tid':tid,
        'tname':tname,
        'tcat':tcat,
        'type':ttype,
        'prc':prc,
        'url':url
    }
    return render(request,'Document.html',Data) 
