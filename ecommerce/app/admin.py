from django.contrib import admin
from app.models import Register

class RegisterAdmin(admin.ModelAdmin):
    list_display=('email','password')

admin.site.register(Register,RegisterAdmin)



    

# Register your models here.
