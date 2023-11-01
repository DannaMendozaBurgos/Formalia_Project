from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import *
import random
from datetime import datetime

def home(request):
    return render(request,'home.html')

def workerSignup(request):
    agents = Agent.objects.all()
    
    if request.method == 'POST':
        vnameWorker = request.POST.get('nameWorker','')
        vcontactWorker = request.POST.get('contactWorker','')
        vmailWorker = request.POST.get('mailWorker','')
        vpasswordWorker = request.POST.get('passwordWorker','')
        vagent = random.choice(agents)
        worker = Worker(nameWorker= vnameWorker,
                    contactWorker= vcontactWorker,
                    mailWorker= vmailWorker,
                    passwordWorker= vpasswordWorker,
                    agent = vagent,
                    )
        worker.save()
    return render(request, 'workerSignup.html')

def EmployerSignup(request):
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
    return render(request, 'EmployerSignup.html')

def setWork(request):
    if request.method == 'POST':
        vtitleWork = request.POST.get('titleWork','')
        vdateWork = request.POST.get('dateWork','')
        vdescriptionWork = request.POST.get('descriptiosWork','')
        vworker = request.POST.get('worker','')
        work = Work(titleWork = vtitleWork,
                    dateWork = vdateWork,
                    descriptionWork = vdescriptionWork,
                    worker=vworker)
        work.save()
    
    return render(request,'SetWork.html')

def setEducation(request):
    if request.method == 'POST':
        vtitleEducation = request.POST.get('titleEducation','')
        vdescriptionEducation = request.POST.get('descriptiosEducation','')
        vinstitution = request.POST.get('institution','')
        vworker = request.POST.get('worker','')
        education = Education(titleEducation = vtitleEducation,
                    institution = vinstitution ,
                    descriptionEducation = vdescriptionEducation,
                    worker=vworker)
        education.save()
    
    return render(request,'SetEducation.html')

def setExperience(request):
    if request.method == 'POST':
        vtitleExperience = request.POST.get('titleExperience','')
        vdescriptionExperience = request.POST.get('descriptiosExperience','')
        vcompanyExperience = request.POST.get('companyExperience','')
        vyearExperience = request.POST.get('yearExperience','')
        vworker = request.POST.get('worker','')
        experience = Experience(titleExperience = vtitleExperience,
                    yearExperience = vyearExperience ,
                    companyExperience = vcompanyExperience ,
                    descriptionExperience = vdescriptionExperience,
                    worker=vworker)
        experience.save()
    
    return render(request,'SetExperience.html')

def AgentSignup(request):
    if request.method == 'POST':
        vnameAgent = request.POST.get('nameAgent','')
        vcontactAgent = request.POST.get('contactAgent','')
        vmailAgent = request.POST.get('mailAgent','')
        vcompanyAgent = request.POST.get('companyAgent','')
        agent = Agent(nameAgent= vnameAgent,
                    contactAgent= vcontactAgent,
                    mailAgent= vmailAgent,
                    companyAgent= vcompanyAgent,)
        agent.save()
    return render(request, 'AgentSignup.html')


def WorkerSignin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        mailWorker = request.POST['mailWorker']
        passwordWorker = request.POST['passwordWorker']
        user = authenticate(request, username=mailWorker, password=passwordWorker)
        if user is not None:
            login(request, user)
            return redirect('home.html') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'WorkerSignin.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'WorkerSignin.html', {'form': form})
    

def newWork(request):
    worker = Worker.objects.all()
    
    if request.method == 'POST':
        vtitleWork = request.POST.get('titleWork','')
        vdescriptionWork = request.POST.get('descriptionWork','')
        vdateWork = request.POST.get('dateWork', '')
        date_format = '%Y-%m-%d'  # Ajusta el formato de fecha según tu formulario HTML
        try:
             dateWork = datetime.strptime(vdateWork, date_format)
        except ValueError:
        
            dateWork = None
        vworker = random.choice(worker)
        work = Worker(titleWork= vtitleWork,
                    descriptionWork= vdescriptionWork,
                    dateWork=dateWork,
                    worker = vworker,
                    )
        work.save()
        

    return render(request, 'setWork.html')
