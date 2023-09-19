from rest_framework import serializers
from .models import student


class studentserializers(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['id','name','roll','city','position']
        