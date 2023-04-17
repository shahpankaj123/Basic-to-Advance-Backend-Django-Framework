from django.db import models
class skill(models.Model):
    skill_name=models.CharField(max_length=20)
    skill_percentage=models.PositiveIntegerField()
    

# Create your models here.
