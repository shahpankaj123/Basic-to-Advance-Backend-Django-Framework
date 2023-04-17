from django.contrib import admin
from service.models import service

class serviceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_desc')

admin.site.register(service,serviceAdmin)
# Register your models here.
