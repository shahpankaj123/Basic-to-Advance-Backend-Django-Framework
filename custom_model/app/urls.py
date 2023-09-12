from django.urls import path,include
from . import views 


urlpatterns = [
    path('',views.home,name="home"),
    path('sendit/',views.sendit,name="sendit"),
    
]