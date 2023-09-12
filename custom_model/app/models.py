from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import Usermanager


class customuser(AbstractUser):
    username=None
    phone_number=models.CharField(max_length=100,unique=True)
    user_bio=models.CharField(max_length=50)
    user_profile=models.FileField(upload_to='profile')
    
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]  
    objects = Usermanager()
    
    
class student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()    

# Create your models here.
