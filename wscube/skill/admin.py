from django.contrib import admin
from skill.models import skill
class skillAdmin(admin.ModelAdmin):
    list_display=('skill_name','skill_percentage')

admin.site.register(skill,skillAdmin)

# Register your models here.
