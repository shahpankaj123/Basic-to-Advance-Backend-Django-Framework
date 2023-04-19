from django.db import models

class Register(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)

# Create your models here.