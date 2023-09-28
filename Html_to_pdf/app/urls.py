
from django.urls import path,include
from app import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('pdf/',views.pdf,name='pdf'),
    path('pdf_view/',views.pdf_view,name='pdf_view'),
]
