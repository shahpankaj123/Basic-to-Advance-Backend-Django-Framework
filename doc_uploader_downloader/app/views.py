from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def home(request):
    pdf_obj=pdf.objects.all()
    return render(request,'index.html',{'data':pdf_obj})



def home1(request):
    if request.method=='POST':
        fl=request.FILES['file']
        name=request.POST['fl']
        pdf.objects.create(pdf_name=name,pdf=fl)
        
    
    return render(request,'form.html',{'data':''})