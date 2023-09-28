from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def home(request):
    pdf_obj=pdf.objects.all()
    return render(request,'index.html',{'data':pdf_obj})
