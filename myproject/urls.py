from django.contrib import admin
from django.urls import path
from . import views as project_views
from website import views as website_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', project_views.home, name='home'),
    path('register/', website_views.register_student, name='register'),
]
