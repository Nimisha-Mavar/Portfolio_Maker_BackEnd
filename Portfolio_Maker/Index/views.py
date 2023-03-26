from django.http import HttpResponse
from django.shortcuts import render,redirect
from Index.models import contact,feedback

# Create your views here.
def home(request):
    return render(request,'index1.html')

def faq(request):
    return render(request,'FAQ.html')

def contact1(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        
        Contact=contact(name=name, email=email ,subject=subject, message=message)
        Contact.save()
        return HttpResponse('Your message has been sent. Thank you!')
    else:
        return HttpResponse('not sent')


def feed(request):
    if request.method == 'POST':
        rate = request.POST['star']
        message = request.POST['Message']
        
        feedback(Rate1=rate, Message1=message).save()
        
        return render(request,'index.html')
    else:
        return render(request,'feedback1.html')
    
    

