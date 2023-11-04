"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from job import views
from job.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
path('',index,name="index"),
path('admin_login',admin_login,name="admin_login"),
path('latest_jobs',latest_jobs,name="latest_jobs"),
path('user_login',user_login,name="user_login"),
path('r_login',r_login,name="r_login"),
path('contact_login',contact_login,name="contact_login"),
path('software_page.html', views.software_page, name='software_page'),
path('aerospace_page.html', views.aerospace_page, name='aerospace_page'),
path('teaching_page.html', views.teaching_page, name='teaching_page'),
path('apply.html', views.apply, name='apply'),
path('notifications.html', views.notifications, name='notifications'),
path('admitcard.html', views.admitcard, name='admitcard'),
path('btech.html', views.btech, name='btech'),
path('examresults.html', views.examresults, name='examresults'),
path('save_enquiry/', views.save_enquiry,name='save_enquiry'),


]
