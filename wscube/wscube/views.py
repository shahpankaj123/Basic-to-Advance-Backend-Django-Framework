from django.http import HttpResponse
from django.shortcuts import render
from skill.models import skill
from contactsave.models import contact_save
from django.core.mail import send_mail

def aboutus(request):
    return HttpResponse("<b>welocme to my websites</b>")

def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data=contact_save(name=name,email=email,subject=subject,message=message)
        data.save()
    return render(request,"index.html")  


def home(request):
    '''send_mail(
        'testing',
        'hello my name is pankaj shah',
        'pankajsha614@gmail.com',
        ['pshah9360@gmail.com'],
        fail_silently=False,)
    '''

    



    skilldata=skill.objects.all()
    data={'skilldata':skilldata}
    return render(request,"index.html",data)
    
def course(request):
    return HttpResponse("<b>course to be choosen</b>")

def coursedetail(request,courseid):
    return HttpResponse(courseid)   


