from django.shortcuts import render,redirect
from .models import Detail
from Services.models import *
from Index.models import feedback
from django.contrib.auth.models import User,auth
# Create your views here.
def Resume_list(request):
    temp="Resume"
    resume=Detail.objects.filter(Temp_cat=temp)
    return render(request,'Template_list.html',{'Temps':resume})

def Portfolio_list(request):
    temp="Portfolio"
    Ports=Detail.objects.filter(Temp_cat=temp)
    return render(request,'Template_list.html',{'Temps':Ports})

def ATS_list(request):
    temp="ATS"
    ATS=Detail.objects.filter(Temp_cat=temp)
    return render(request,'Template_list.html',{'Temps':ATS})

def temp_detail(request,id):
    data=Detail.objects.get(id=id)
    feed=feedback.objects.filter(Template_id=id)
    context={
         'data':data,
         'feed':feed
    }
    return render(request,'Template_detail.html',context)

#forms and REsuem and portfolio insert logic
def form(request):
    Cat=request.POST["cat"]
    T_id=request.POST["id"]
    u_id=request.user
    if Cat=="Portfolio":
            if Portfolio.objects.filter(Template_id=T_id,User_id=u_id.id).exists():
                 err= {
                      'msg':"Already selected by you",
                      'ttl':"Already Exist",
                      'active':'True',
                      'temp_cat':Cat,
                      'temp_id':T_id
                 }
                 return render(request,'Error.html',err)
            else:
                port_id=Portfolio.objects.only('Portfoli_id').count()
                port_id+=1
                try:
                    Port=Portfolio(Portfolio_id=port_id,Template_id=T_id,User_id=u_id.id)
                    Port.save()
                    Pid=Port.Portfolio_id
                    print(Pid)
                    return render(request,'Portfolio_form.html',{'Portid':Pid})
                except:
                    err= {
                      'msg':"Template use after login",
                      'ttl':"Login requierd",
                      'log':'True'
                    }
                    return render(request,'Error.html',err)
                
    else:
            if Resume.objects.filter(Template_id=T_id,User_id=u_id.id):
                err= {
                      'msg':"Already selected by you",
                      'ttl':"Already Exist",
                      'active':'True',
                      'temp_cat':Cat,
                      'temp_id':T_id
                 }
                return render(request,'Error.html',err)
            else:
                res_id=Resume.objects.only('Resume_id').count()
                res_id+=1
                try:
                    Res=Resume(Resume_id=res_id,Template_id=T_id,User_id=u_id.id)
                    Res.save()
                    R_id=Res.Resume_id
                    return render(request,'Resume_form.html',{'Resid':R_id})
                except:
                    err= {
                      'msg':"Template used after login",
                      'ttl':"Login requierd",
                      'log':'True'
                    }
                    return render(request,'Error.html',err)
            
#selected template delete
def select_dlt(request):
    cat=request.POST['t_cat']
    temp_id=request.POST['t_id']
    u_id=request.user
    if cat=="Portfolio":
         Port=Portfolio.objects.get(Template_id=temp_id,User_id=u_id.id)
         Port.delete()
         return redirect('Portfolio-list')
    else:
         Res=Resume.objects.get(Template_id=temp_id,User_id=u_id.id)
         Res.delete()
         return redirect('Resume-list')
    

def edit(request):
    cat=request.POST['Ccat']
    idd=request.POST['id']
    if cat=="Portfolio":
        edu=Education.objects.filter(Portfolio_id=idd)
        ex=Experience.objects.filter(Portfolio_id=idd)
        proj=Project.objects.filter(Portfolio_id=idd)
        skill=Skill.objects.filter(Portfolio_id=idd)
        award=Award.objects.filter(Portfolio_id=idd)
        social=Social_Media.objects.filter(Portfolio_id=idd)
        contaxt={
            'Portid':idd,
            'edu':edu,
            'ex':ex,
            'pro':proj,
            'sk':skill,
            'awd':award,
            'scl':social
        }
        return render(request,'Portfolio_form.html',contaxt)
    else:
        edu=Education.objects.filter(Resume_id=idd)
        ex=Experience.objects.filter(Resume_id=idd)
        proj=Project.objects.filter(Resume_id=idd)
        skill=Skill.objects.filter(Portfolio_id=idd)
        contaxt={
            'resid':idd,
            'edu':edu,
            'ex':ex,
            'pro':proj,
            'sk':skill
        }
        return render(request,'Resume_form.html')
    