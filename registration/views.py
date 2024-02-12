from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def registerFunction(request):
    error_message=None
    if request.method=='POST':
        uname=request.POST['name']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['Confirmpassword']
        
        if pass1!=pass2:
            error_message='Your password and Confirm password must be same'
        else:
            myUser=User.objects.create_user(uname,email,pass1)
            myUser.save()
            return redirect('login')
    return render(request,'signup.html',{'error_message':error_message})



def loginFunction(request):
    error_message=None
    if(request.method=='POST'):
        username=request.POST['username']
        pass1=request.POST['password']
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html',{'error_message':error_message})

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')
    
def logout(request):
    return redirect('login')  
# Create your views here.
