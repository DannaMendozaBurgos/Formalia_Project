from django.urls import path, include
from django.contrib import admin
from . import views
 
urlpatterns = [
    path('workerlogin/', views.workerlogin, name='workerlogin'),
]