from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student
from .serializers import studentserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import messages

     
@api_view(['GET'])
def home(request):
    stu=student.objects.all()
    serializer=studentserializers(stu,many=True)
    return render(request,'index.html',{'data':serializer.data})
    



@api_view(['POST'])
def studentcreate(request):
    serializer=studentserializers(data=request.data)
    
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':'False','Message':'Send unsuccessfull'})
    serializer.save()
    messages.success(request, "Profile created successfully.")
    return redirect('/')


@api_view(['PATCH'])
def studentupdate(request,pk):
    stu=student.objects.get(id=pk)
    serializer=studentserializers(stu,data=request.data,partial=True)
    
    if not serializer.is_valid():
        return Response({'status':'False','Message':'update unsuccessfull'})
    
    serializer.save()
    return Response({'status':'True','Message':'update successfully'})



def studentdelete(request,pk):
    stu=student.objects.get(id=pk)
    stu.delete()
    messages.success(request, "Data Deleted")
    return redirect('/')
    
   
        
    
        
    
        
    

# Create your views here.
