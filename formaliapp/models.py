from django.db import models


class Agent(models.Model):
    
    id = models.AutoField(primary_key=True, db_column='idAgent')
    nameAgent = models.CharField(max_length=45)
    contactAgent = models.CharField(max_length=45)
    mailAgent = models.CharField(max_length=45)
    companyAgent = models.CharField(max_length=45)
    class Meta:
        managed = False
        db_table = 'Agent'

class Worker(models.Model):
    id = models.AutoField(primary_key=True, db_column='idWoker')
    nameWorker = models.CharField(max_length=45)
    contactWorker = models.CharField(max_length=45)
    mailWorker = models.EmailField()
    passwordWorker = models.CharField(max_length=45)
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING, db_column='Agent_idAgent')
    class Meta:
        managed = False
        db_table = 'Worker'

class Employer(models.Model):
    id = models.AutoField(primary_key=True, db_column='idEmployer')
    nameEmployer = models.CharField(max_length=45)
    contactEmployer = models.CharField(max_length=45)
    mailEmployer = models.CharField(max_length=45)
    passwordEmployer = models.CharField(max_length=45)
    companyEmployer = models.CharField(max_length=45)
    class Meta:
        managed = False
        db_table = 'Employer'

type_contract = [
    ('service', 'Service'),
    ('limit', 'Limit'),
]        

class Contract(models.Model):
    id = models.AutoField(primary_key=True, db_column='idContract')
    typeContract = models.CharField(max_length=20, choices=type_contract)
    startdate = models.DateField()
    finishdate = models.DateField()
    fareContract = models.IntegerField()
    descriptionContract = models.TextField()    
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE, db_column='Worker_idWoker')
    employer = models.ForeignKey(Employer,on_delete=models.CASCADE,db_column='Employer_idEmployer')
    class Meta:
        managed = False
        db_table = 'Contract'

class Work(models.Model):
    id = models.AutoField(primary_key=True, db_column='idWork')
    titleWork = models.CharField(max_length=45)
    dateWork = models.DateField()
    descriptionWork = models.TextField()
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, db_column='Worker_idWoker')
    class Meta:
        managed = False
        db_table = 'Work'

class Education(models.Model):
    id = models.AutoField(primary_key=True, db_column='idEducation')
    titleEducation = models.CharField(max_length=45)
    descriptionEducation = models.TextField()
    institution = models.CharField(max_length=45)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'Education'

class Experience(models.Model):
    id = models.AutoField(primary_key=True, db_column='idExperience')
    titleExperience = models.CharField(max_length=45)
    descriptionExperience = models.TextField()
    companyExperience = models.CharField(max_length=45)
    yearExperience = models.DateField()
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'Experience'



