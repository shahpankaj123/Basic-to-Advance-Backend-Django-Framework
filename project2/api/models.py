from django.db import models


class student1(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    roll_no=models.IntegerField()
    