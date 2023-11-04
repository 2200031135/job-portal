# your_app/models.py

from django.db import models


class JobListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Add other fields like location, company, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title



# Create your models here.
from django.db import models





class Userregistration(models.Model):
    id=models.AutoField(blank=False,primary_key=True)
    username = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def str(self):
        return self.username

class adminlogin(models.Model):
    id=models.AutoField(blank=False,primary_key=True)
    username = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def str(self):
        return self.username

class recruiterlogin(models.Model):
    id=models.AutoField(blank=False,primary_key=True)
    username = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def str(self):
        return self.username
class userlogin(models.Model):
    id=models.AutoField(blank=False,primary_key=True)
    username = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def str(self):
        return self.username


def applyform():
    return


class ApplyForm(models.Model):
    fullname = models.CharField(max_length=100, help_text="Full Name")
    email = models.EmailField(max_length=100, help_text="Email Address")
    phone = models.CharField(max_length=15, help_text="Phone Number")
    address = models.TextField(help_text="Address")
    previous_experience = models.TextField(null=True, default="")
    years_of_experience = models.IntegerField(null=True, default="")

    EDUCATION_LEVEL_CHOICES = (
        ('High School', 'High School'),
        ("Bachelor's Degree", "Bachelor's Degree"),
        ("Master's Degree", "Master's Degree"),
        ('PhD', 'PhD'),
    )
    highest_education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES,
                                               help_text="Highest Education Level")

    university = models.CharField(max_length=100, help_text="University")

    def __str__(self):
        return self.fullname

