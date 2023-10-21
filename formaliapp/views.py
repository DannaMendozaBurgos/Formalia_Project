from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import *

def workerlogin(request):
    if request.method == 'POST':
        vnameWorker = request.POST.get('nameWorker','')
        vcontactWorker = request.POST.get('contactWorker','')
        vmailWorker = request.POST.get('mailWorker','')
        vpasswordWorker = request.POST.get('passwordWorker','')
        worker = Worker(nameWorker= vnameWorker,
                    contactWorker= vcontactWorker,
                    mailWorker= vmailWorker,
                    passwordWorker= vpasswordWorker,)
        worker.save()
    return render(request, 'formaliapp/workerLogin.html')

def Employerlogin(request):
    if request.method == 'POST':
        vnameEmployer = request.POST.get('nameEmployer','')
        vcontactEmployer = request.POST.get('contactEmployer','')
        vmailEmployer = request.POST.get('mailEmployer','')
        vpasswordEmployer = request.POST.get('passwordEmployer','')
        vcompanyEmployer = request.POST.get('companyEmployer','')
        emplo = Employer(nameEmployer= vnameEmployer,
                    contactEmployer= vcontactEmployer,
                    mailEmployer= vmailEmployer,
                    passwordEmployer= vpasswordEmployer,
                    companyEmployer= vcompanyEmployer,)
        emplo.save()
    return render(request, 'formaliapp/EmployerLogin.html')

def setWork(request):
    if request.method == 'POST':
        vtitleWork = models
