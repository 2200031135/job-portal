# Generated by Django 4.2.4 on 2023-11-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_adminlogin_recruiterlogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(help_text='Full Name', max_length=100)),
                ('email', models.EmailField(help_text='Email Address', max_length=254, unique=True)),
                ('phone', models.CharField(help_text='Phone Number', max_length=15)),
                ('address', models.TextField(help_text='Address')),
                ('previous_experience', models.TextField(help_text='Previous Experience')),
                ('years_of_experience', models.PositiveIntegerField(help_text='Years of Experience')),
                ('highest_education_level', models.CharField(choices=[('High School', 'High School'), ("Bachelor's Degree", "Bachelor's Degree"), ("Master's Degree", "Master's Degree"), ('PhD', 'PhD')], help_text='Highest Education Level', max_length=20)),
                ('university', models.CharField(help_text='University', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userlogin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('repassword', models.CharField(max_length=20)),
            ],
        ),
    ]
