from django.db import models

# Create your models here.

class pdf(models.Model):
    pdf_name=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='mypdf')
