from django.contrib import admin
from contactsave.models import contact_save

class contactAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message')

admin.site.register(contact_save,contactAdmin)    


# Register your models here.
