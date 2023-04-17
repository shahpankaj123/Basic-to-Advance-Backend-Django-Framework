from django.db import models

class contact_save(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=200)
    


# Create your models here.
