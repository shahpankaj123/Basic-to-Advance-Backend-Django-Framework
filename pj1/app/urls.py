from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('student/',views.studentget.as_view()),
    path('studentcreate/',views.studentcreate.as_view()),
    path('studentRetrive/<int:pk>',views.studentRetrive.as_view()),
    path('studentupdate/<int:pk>',views.studentupdate.as_view()),
    path('studentdelete/<int:pk>',views.studentdelete.as_view()),
    
]