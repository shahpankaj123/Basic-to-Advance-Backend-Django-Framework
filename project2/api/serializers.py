from .models import *
from rest_framework import serializers

class studentserializer1(serializers.ModelSerializer):
    
    class Meta:
        model=student1
        fields='__all__'