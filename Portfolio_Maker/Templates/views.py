from django.shortcuts import render,redirect
from .models import Detail
from Services.models import Portfolio,Resume
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
    return render(request,'Template_detail.html',{'data':data})

def form(request):
    Cat=request.POST["cat"]
    T_id=request.POST["id"]
    u_id=request.user
    if Cat=="Portfolio":
            if Portfolio.objects.filter(Template_id=T_id,User_id=u_id.id).exists():
                 err= {
                      'msg':"Already selected by you",
                      'ttl':"Already Exist"
                 }
                 return render(request,'Error.html',err)
            else:
                port_id=Portfolio.objects.only('Portfoli_id').count()
                port_id+=1
                try:
                    Port=Portfolio(Portfolio_id=port_id,Template_id=T_id,User_id=u_id.id)
                    Port.save()
                    Pid=Port.Portfolio_id
                    return render(request,'Portfolio_form.html',{'Portid':Pid})
                except:
                    err= {
                      'msg':"Used after login",
                      'ttl':"Login requierd"
                    }
                    return render(request,'Error.html',err)
                
    else:
            if Resume.objects.filter(Template_id=T_id,User_id=u_id.id):
                err= {
                      'msg':"Already selected by you",
                      'ttl':"Already Exist"
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
                      'msg':"Used after login",
                      'ttl':"Login requierd"
                    }
                    return render(request,'Error.html',err)
            
def err(request):
     return render(request,'Error.html')