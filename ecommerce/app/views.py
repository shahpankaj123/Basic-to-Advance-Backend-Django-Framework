from django.shortcuts import render
from app.models import Register
from app.models import Product_detail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
 data=Product_detail.objects.all()
 productdata={'data':data}
 return render(request, 'app/home.html',productdata)


def product_detail(request):
 return render(request, 'app/productdetail.html')

@login_required(login_url='login')
def add_to_cart(request):
 return render(request, 'app/addtocart.html')

@login_required(login_url='login')
def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required(login_url='login')
def profile(request):
 return render(request, 'app/profile.html')

@login_required(login_url='login')
def address(request):
 return render(request, 'app/address.html')

@login_required(login_url='login')
def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

@login_required(login_url='login')
def mobile(request):
 return render(request, 'app/mobile.html')


def Login(request): 
  name=""
  if request.method == 'POST':
   email=request.POST.get('email')
   pass1= request.POST.get('password')
   name=email
   myuser = authenticate(username=email,password=pass1)
   if myuser is not None:
    login(request,myuser)
    return render(request,'app/home.html',{'name':name})
   else:
    messages.warning(request,"Password or Username donot match")
    return render(request, 'app/login.html') 
  else:  
   return render(request, 'app/login.html') 

def customerregistration(request):
  if request.method=='POST':
   email=request.POST.get('email')
   password=request.POST.get('password')
   c_password=request.POST.get('c_password')
   if password==c_password:
    my_user=User.objects.create_user(email,email,password)
    my_user.save()
    return render(request,'app/login.html')
    messages.success(request,"Register successfull! please login")
   else:
      messages.warning(request,"Register Unsuccessfull! please check your password and email")
  return render(request, 'app/customerregistration.html')

@login_required(login_url='login')
def checkout(request):
 return render(request, 'app/checkout.html')

def Logout(request):
 logout(request)
 return render(request, 'app/login.html')
