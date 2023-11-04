from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.admin_login, name='admin_login'),
    path('save_enquiry/', views.save_enquiry,name='save_enquiry'),

]