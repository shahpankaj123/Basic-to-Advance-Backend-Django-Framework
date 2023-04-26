from django.contrib import admin
from app.models import Register
from app.models import  product

class RegisterAdmin(admin.ModelAdmin):
    list_display=('email','password')

admin.site.register(Register,RegisterAdmin)
admin.site.register(product)




    

# Register your models here.
