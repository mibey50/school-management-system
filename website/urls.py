from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='home'),
    path('register/', views.register_student, name='register'),
]