from django.shortcuts import render
from Templates.models import Detail
from Services.models import Portfolio,Resume
# Create your views here.
def dashboard(request):
    u_id=request.user
    #for document
    port=Portfolio.objects.filter(User_id=u_id.id)
    res=Resume.objects.filter(User_id=u_id.id)
    doc={
        'Port':port,
        'Res':res,
    }
    return render(request,'dashboard.html',doc)