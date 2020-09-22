"""aishwarya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emotion_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.home),
    path(r'dashboard/', views.dashboard),
    path(r'login/', views.login, name='login'),
    path(r'logout/', views.logout, name='logout'),
    path(r'open_camera/', views.open_camera),
    path(r'process-image/', views.process_image),
    path(r'upload-new-song/', views.upload_new_song),
    path(r'reset/', views.reset, name='reset'),
]
