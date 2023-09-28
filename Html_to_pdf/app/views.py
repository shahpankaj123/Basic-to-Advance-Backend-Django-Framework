from django.shortcuts import render
from django.http import HttpResponse
from .pdf import *
from .models import *



def home(request):
    return render(request,'index.html')

def pdf_view(request):
    student_obj=student.objects.all()
    return render(request,'pdf.html',{'data':student_obj})

def pdf(request):
    student_obj=student.objects.all()
    pdf_data=pdf_conveter('pdf.html',{'data':student_obj})
    return HttpResponse(pdf_data,content_type='application/pdf')

# Create your views here.
