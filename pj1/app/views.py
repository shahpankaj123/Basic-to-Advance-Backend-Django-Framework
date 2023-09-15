from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.mixins import *
from rest_framework.generics import GenericAPIView
from .models import student
from .serializers import studentserializer


# Create your views here.

class studentget(GenericAPIView,ListModelMixin):
    queryset=student.objects.all()
    serializer_class=studentserializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
 
    
class studentcreate(GenericAPIView,CreateModelMixin):
    queryset=student.objects.all()
    serializer_class=studentserializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
 

class studentRetrive(GenericAPIView,RetrieveModelMixin):
    queryset=student.objects.all()
    serializer_class=studentserializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs) 
    

class studentupdate(GenericAPIView,UpdateModelMixin):
    queryset=student.objects.all()
    serializer_class=studentserializer
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs) 
    
class studentdelete(GenericAPIView,DestroyModelMixin):
    queryset=student.objects.all()
    serializer_class=studentserializer
    
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)           
    
