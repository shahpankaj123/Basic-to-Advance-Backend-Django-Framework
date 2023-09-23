from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='Login')
def home(request):
    return render(request,'home.html')


def Login_page(request):
    return render(request,'login.html')

def signup_page(request):
    return render(request,'signup.html')
    
def Logout(request):
    logout(request)
    return redirect('/')


    
