from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def Register(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password1']
        password1=request.POST['password2']

        if password==password1:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('Register')
            else:
                user=User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username,  password=password)
                user.save();
                print('user created')
                return render(request,'Login.html')
            
        else:
            print('Password does not match')
            
    else:
        return render(request,'Register.html')
    

def login(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            return redirect('login')

    else:
     return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')