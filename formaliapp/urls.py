from django.urls import path, include
from django.contrib import admin
from . import views
 
urlpatterns = [
    path('',views.home, name='home'),
    path('workerSignup/', views.workerSignup, name='workerSignup'),
    path('AgentSignup/', views.AgentSignup, name='AgentSignup'),
    path('EmployerSignup/', views.EmployerSignup, name='EmployerSignup'),
    path('WorkerSignin/', views.WorkerSignin, name='WorkerSignin'),
    path('newWork/', views.newWork, name='newWork'),
    path('newContract/', views.newContract, name='newContract'),
    
    
]
