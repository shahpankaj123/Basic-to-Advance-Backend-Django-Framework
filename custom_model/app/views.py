from django.shortcuts import render,redirect
from .utils import *


def home(request):
   return render(request,"index.html")
def sendit(request):
    sendmail()
    return redirect("/")
     
# Create your views here.
