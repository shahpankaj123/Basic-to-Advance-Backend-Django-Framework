from django.db import models
class product(models.Model):
    product_name=models.CharField(max_length=100)
    product_category=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=200)
    product_price=models.PositiveIntegerField()
    product_discount=models.PositiveIntegerField()
    product_img=models.FileField(upload_to="app/static/images/upload",max_length=250,null=True,default=None)



# Create your models here.
