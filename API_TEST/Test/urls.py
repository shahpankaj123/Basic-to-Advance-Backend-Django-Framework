from django.urls import path,include
from .views import *


urlpatterns = [
    path('',home),
    path('post_student',post_student),
    path('student_update/<id>/',student_update),
    path('student_delete/<id>/',student_delete),
    path('Test',Test.as_view()),
    
]