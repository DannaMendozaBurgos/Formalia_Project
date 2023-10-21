# Generated by Django 4.2.1 on 2023-10-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('idAgent', models.IntegerField(primary_key=True, serialize=False)),
                ('nameAgent', models.CharField(max_length=45)),
                ('contactAgent', models.CharField(max_length=45)),
                ('mailAgent', models.CharField(max_length=45)),
                ('companyAgent', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Agent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('idContract', models.IntegerField(primary_key=True, serialize=False)),
                ('typeContract', models.CharField(choices=[('service', 'Service'), ('limit', 'Limit')], max_length=20)),
                ('startdate', models.DateField()),
                ('finishdate', models.DateField()),
                ('fareContract', models.IntegerField()),
                ('descriptionContract', models.TextField()),
            ],
            options={
                'db_table': 'Contract',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('idEducation', models.IntegerField(primary_key=True, serialize=False)),
                ('titleEducation', models.CharField(max_length=45)),
                ('descriptionEducation', models.TextField()),
                ('institution', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Education',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('idEmployer', models.IntegerField(primary_key=True, serialize=False)),
                ('nameEmployer', models.CharField(max_length=45)),
                ('contactEmployer', models.CharField(max_length=45)),
                ('mailEmployer', models.CharField(max_length=45)),
                ('passwordEmployer', models.CharField(max_length=45)),
                ('companyEmployer', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Employer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('idEducation', models.IntegerField(primary_key=True, serialize=False)),
                ('titleExperience', models.CharField(max_length=45)),
                ('descriptionExperience', models.TextField()),
                ('companyExperience', models.CharField(max_length=45)),
                ('yearExperience', models.DateField()),
            ],
            options={
                'db_table': 'Experience',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('idWork', models.IntegerField(primary_key=True, serialize=False)),
                ('titleWork', models.CharField(max_length=45)),
                ('dateWork', models.DateField()),
                ('descriptionWork', models.TextField()),
            ],
            options={
                'db_table': 'Work',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('idWorker', models.IntegerField(primary_key=True, serialize=False)),
                ('nameWorker', models.CharField(max_length=45)),
                ('contactWorker', models.CharField(max_length=45)),
                ('mailWorker', models.EmailField(max_length=254)),
                ('passwordWorker', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Worker',
                'managed': False,
            },
        ),
    ]
