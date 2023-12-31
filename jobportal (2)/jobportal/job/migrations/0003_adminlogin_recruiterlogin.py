# Generated by Django 4.2.4 on 2023-10-15 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_userregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminlogin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('repassword', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='recruiterlogin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('repassword', models.CharField(max_length=20)),
            ],
        ),
    ]
