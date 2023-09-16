from django.shortcuts import render
from .models import student1
from .serializers import studentserializer1
from rest_framework import viewsets
from rest_framework.authentication import *
from rest_framework.permissions import *


class studentmodelapi(viewsets.ModelViewSet):
    queryset=student1.objects.all()
    serializer_class=studentserializer1
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
# Create your views here.
