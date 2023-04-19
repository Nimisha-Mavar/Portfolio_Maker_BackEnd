from django.shortcuts import render,HttpResponse,redirect
from Templates.models import Detail
from Services.models import Portfolio,Resume
from .models import Favourite
# Create your views here.
def dashboard(request):
    u_id=request.user
    #for document
    port=Portfolio.objects.filter(User_id=u_id.id)
    res=Resume.objects.filter(User_id=u_id.id)
    fav=Favourite.objects.filter(User_id=u_id.id)
    doc={
        'Port':port,
        'Res':res,
        'Fav':fav
    }
    return render(request,'dashboard.html',doc)

def favourite(request):
    tid=request.POST['tid']
    uid=request.user
    if Favourite.objects.filter(Template_id=tid,User_id=uid.id).exists():
        return redirect('Dashboard')
    else:
        obj=Favourite(Template_id=tid,User_id=uid.id)
        obj.save()
        return redirect('Dashboard')
    
def fav_del(request,id):
    obj=Favourite.objects.filter(id=id)
    obj.delete()
    print(obj)
    return redirect('Dashboard')
