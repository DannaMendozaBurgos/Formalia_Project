from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .models import *
import random
from datetime import datetime
from django.shortcuts import get_object_or_404


def home(request):
    return render(request,'index.html')

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
    return render(request, 'WorkerSignup.html')

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
        work = Work(titleWork= vtitleWork,
                    descriptionWork= vdescriptionWork,
                    dateWork=dateWork,
                    worker = vworker,
                    )
        work.save()
        

    return render(request, 'setWork.html')

def newContract(request):
   
    employers = Employer.objects.all()
    type_contract_choices = [('Service', 'Service'), ('Limit', 'Limit')]
    workers = Worker.objects.all()
    
    if request.method == 'POST':
        vtype = request.POST.get('typeContract','')
        vstart = request.POST.get('startdate','')
        vfinish = request.POST.get('finishdate','')
        vdescription = request.POST.get('descriptionContract','')
        vfare = request.POST.get('fareContract','')
        vworker_id = request.POST.get('worker', '')  # Get the worker ID
        vemployer_id = request.POST.get('employer', '')  # Get the employer ID

        vstart = datetime.strptime(vstart, '%Y-%m-%d').date()
        vfinish = datetime.strptime(vfinish, '%Y-%m-%d').date()
        #vworker = Worker.objects.get(pk=vworker)
        #vemployer = Employer.objects.get(pk=vemployer)

        vworker = get_object_or_404(Worker, pk=vworker_id)
        vemployer = get_object_or_404(Employer, pk=vemployer_id)

        contract = Contract(typeContract = vtype,
                            startdate=vstart,
                            finishdate=vfinish,
                            descriptionContract = vdescription,
                            fareContract = vfare,
                            worker = vworker,
                            employer = vemployer
        )

        contract.save()

    return render(request, 'Contract.html', {'type_contract_choices': type_contract_choices,'workers': workers,
        'employers': employers})