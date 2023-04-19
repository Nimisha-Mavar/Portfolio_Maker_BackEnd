from django.shortcuts import render
from Services.models import *
from payment.models import Payment
# Portfolio Templates
def Basic_pf_1(request):
    return render(request,'D_Basic_Pf_1.html')

def Basic_pf_2(request):
    return render(request,'D_Basic_Pf_2.html')

def Premium_pf_1(request):
    return render(request,'D_Premium_Pf_1.html')

def Premium_pf_2(request):
    return render(request,'D_Premium_Pf_2.html')

def iportfolio(request):
    if request.method=='GET':
        pid=request.GET['pid']
        u_id=request.user
        contaxt=Portfolio_data(pid,u_id)
        return render(request,'Premium_Pf_3.html',contaxt)
    else:
        return render(request,'D_Premium_Pf_3.html')

# Resume Template
def Basic_Rm_1(request):
    if request.method=='GET':
        pid=request.GET['pid']
        u_id=request.user
        contaxt=Resume_data(pid,u_id)
        return render(request,'Basic_Resume_1.html',contaxt)
    else:
        return render(request,'D_Basic_Resume_1.html')

def Basic_Rm_2(request):
    return render(request,'Premium_R_2.html')

def Premium_Rm_1(request):
    return render(request,'Premium_R_1.html')

def Premium_Rm_2(request):
    if request.method=='GET':
        pid=request.GET['pid']
        u_id=request.user
        contaxt=Resume_data(pid,u_id)
        return render(request,'Premium_R_3.html',contaxt)
    else:
        return render(request,'Premium_R_3.html')

def Resume_data(pid,u_id):
        prs=Personal_info.objects.filter(User_id=u_id.id)
        edu=Education.objects.filter(Resume_id=pid)
        ex=Experience.objects.filter(Resume_id=pid)
        proj=Project.objects.filter(Resume_id=pid)
        skill=Skill.objects.filter(Resume_id=pid)
        contaxt={
            'prs':prs,
            'edu':edu,
            'ex':ex,
            'pro':proj,
            'sk':skill,
            'active':True
        }
        return contaxt

def Portfolio_data(pid,u_id):
        prs=Personal_info.objects.filter(User_id=u_id.id)
        edu=Education.objects.filter(Portfolio_id=pid)
        ex=Experience.objects.filter(Portfolio_id=pid)
        proj=Project.objects.filter(Portfolio_id=pid)
        skill=Skill.objects.filter(Portfolio_id=pid)
        award=Award.objects.filter(Portfolio_id=pid)
        social=Social_Media.objects.filter(Portfolio_id=pid)
        contaxt={
            'prs':prs,
            'edu':edu,
            'ex':ex,
            'pro':proj,
            'sk':skill,
            'awd':award,
            'scl':social
        }
        return contaxt