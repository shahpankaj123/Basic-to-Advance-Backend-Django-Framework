from django.urls import path,include
from api import views

urlpatterns = [
    
    path('',views.home),
    path('studentcreate/',views.studentcreate,name='createstu'),
    path('studentupdate/<int:pk>',views.studentupdate),
    path('studentdelete/<int:pk>',views.studentdelete,name="delete"),
    
]