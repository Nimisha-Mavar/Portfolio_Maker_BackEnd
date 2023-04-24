from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password
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
                msg="Email exist."
                return render(request,'Register.html',{'msg':msg}) 
            elif User.objects.filter(username=username).exists():
                msg="Username exist."
                return render(request,'Register.html',{'msg':msg}) 
            else:
                user=User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username,  password=password)
                user.save();
                print('user created')
                return render(request,'Login.html')
            
        else:
            msg="Password doesn't match."
            return render(request,'Register.html',{'msg':msg}) 
            
    else:
        return render(request,'Register.html')
    

def login(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('password') 
        if username=='' and password=='':
            msg="Please enter username and password."
            return render(request,'Login.html',{'msg':msg}) 
        elif username=='':
            msg="Please enter username."
            return render(request,'Login.html',{'msg':msg}) 
        elif password=='':
            msg="Please enter password."
            return render(request,'Login.html',{'msg':msg})
        else:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                msg="Invalid Username and password."
                return render(request,'Login.html',{'msg':msg})
            
    else:
     return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def forgot_password(request):
    if request.method == 'POST':
        uname=request.POST['usernm']
        if User.objects.filter(username=uname).exists():
            return render(request, 'forgot_pass1.html',{'uname':uname})
        else:
            return render(request, 'forgot_password.html')
    else:
        return render(request, 'forgot_password.html')

#logic of forgot password
def set_pass(request):
    npass=request.POST['newpass']
    cpass=request.POST['cpass']
    unm=request.POST['uname']
    if npass==cpass:
        u = User.objects.get(username=unm)
        u.set_password(npass)
        u.save()
        return redirect('Login')
    else:
        return render(request, 'forgot_pass1.html')

#logic for change password
def cng_pass(request):
    npass=request.POST['npass']
    cpass=request.POST['cpass']
    u_id=request.user
    u = User.objects.get(id=u_id.id)
    print(u.username)
    print(u.password)
    if check_password(cpass,u.password):
        u.set_password(npass)
        u.save()
        logout(request)
        return redirect('Login')
    else:
        return render(request,'dashboard.html',{'msg':"Password does not match.."})
