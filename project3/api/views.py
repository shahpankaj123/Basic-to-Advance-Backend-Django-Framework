from django.shortcuts import render
from rest_framework import viewsets
from .models import student
from .serializers import studentserializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import *



class studentapi(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=studentserializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
class studentlist(ListAPIView):
    queryset=student.objects.all()
    serializer_class=studentserializer
    
class studentupdate(UpdateAPIView):
    queryset=student.objects.all()
    serializer_class=studentserializer
        
        


# Create your views here.
