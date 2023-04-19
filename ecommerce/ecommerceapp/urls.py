from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index,name="home"),
]