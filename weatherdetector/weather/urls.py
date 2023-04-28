from django.contrib import admin
from django.urls import path
from weather import views

urlpatterns = [
    path('',views.home,name='home'),
]