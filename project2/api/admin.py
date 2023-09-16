from django.contrib import admin
from .models import *



@admin.register(student1)
class studentadmin1(admin.ModelAdmin):
    list_display=['id','name','age','roll_no']