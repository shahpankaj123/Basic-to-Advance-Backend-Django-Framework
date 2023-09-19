from django.db import models



class student(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    city=models.CharField(max_length=50)
    position=models.CharField(max_length=5,unique=True)

# Create your models here.
