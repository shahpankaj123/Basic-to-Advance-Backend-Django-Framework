from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        myuser = authenticate(username=username,password=password)
        if myuser is not None:
         login(request,myuser)
         return redirect('home')
        else:
          messages.warning(request,"Password or Username donot match")   
    return render(request,'login.html')
def signup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if User.objects.filter(username=username):
            messages.warning(request,"Username Already Taken")
            return render(request,'signup.html')

        if password2==password1:      
            my_user=User.objects.create_user(username,"",password1)
            my_user.save()
            messages.success(request,"Account created successfully")
            return redirect('Login')
        else:
            messages.warning(request,"Please type same password")
            return redirect('signup')
        
    return render(request,'signup.html')
def Logout(request):
   logout(request)
   return redirect('Login')

@login_required(login_url='login.html')
def home(request):
   return render(request,'home.html')