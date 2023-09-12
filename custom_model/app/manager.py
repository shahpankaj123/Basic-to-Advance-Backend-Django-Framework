from typing import Any
from django.contrib.auth.base_user import BaseUserManager


class Usermanager(BaseUserManager):
    
    def create_user(self,phone_number,password=None,**extra_fields):
        if not phone_number:
            raise ValueError("phone number is required")
        
        user=self.model(phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        
        return user
    
    def create_superuser(self,phone_number,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        return self.create_user(phone_number,password,**extra_fields)