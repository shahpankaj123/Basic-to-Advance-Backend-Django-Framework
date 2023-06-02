from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .models import *
from .serializers import *
from rest_framework.views import APIView

@api_view(['GET'])
def home(request):
    student_obj=student.objects.all()
    serializer=studentserializer(student_obj,many=True)
    
    
    return Response({'status':'True','data':serializer.data})

@api_view(['POST'])
def post_student(request):
    serializer=studentserializer(data=request.data)
    
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({'status':'False','Message':'Send unsuccessfull'})
    serializer.save()
        
    
    return Response({'status':'True','data':serializer.data,'Message':'Send successfull'})
        
@api_view(['PUT'])
def student_update(request, id):
    try:
        student_obj=student.objects.get(id = id)
        serializer=studentserializer(student_obj,data=request.data,partial=True)
        if not serializer.is_valid():
         print(serializer.errors)
         return Response({'status':'True','Message':'update unsuccessfull'})
        serializer.save()
        return Response({'status':'True','data':serializer.data,'Message':'updated successfull'})
    except Exception as e:
        return Response({'status':'400','error':'error found'})
    
    
@api_view(['DELETE'])    
def student_delete(request, id):
    try:
        student_obj=student.objects.get(id = id)
        student_obj.delete()
        return Response({'status':'True','Message':'delted successfull'})
    except Exception as e:
        return Response({'status':'400','error':'error found'})
    
        
class Test(APIView):
    def get(self, request):
        
      student_obj=student.objects.all()
      serializer=studentserializer(student_obj,many=True)
      return Response({'status':'True','data':serializer.data})
    
    def post(self, request):
        serializer=studentserializer(data=request.data)
    
        if not serializer.is_valid():
         print(serializer.errors)
         return Response({'status':'False','Message':'Send unsuccessfull'})
        serializer.save()
        return Response({'status':'True','data':serializer.data,'Message':'Send successfull'})
        
        
        
      
      
        

