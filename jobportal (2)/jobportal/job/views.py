from django.db.models import Q
from django.shortcuts import render
from job.models import ApplyForm

from job.models import Userregistration, recruiterlogin,userlogin


# Create your views here.
def index(request):
    return render(request,'index.html')
def admin_login(request):
    context = {'message':'Invalid Credentials......'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = Userregistration.objects.filter(Q(username=username),  Q(password=password))
        if data:
            return render(request,'loginsuccess.html')
        else:
            return render(request,'loginsuccess.html',context)
    return render(request, 'admin_login.html')
def latest_jobs(request):
    return render(request,'latest_jobs.html')
def user_login(request):
    return render(request,'user_login.html')
def r_login(request):
    return render(request,'r_login.html')
def contact_login(request):
    return render(request,'contact_login.html')

def software_page(request):
    return render(request,'software_page.html')

def teaching_page(request):
    return render(request,'teaching_page.html')

def aerospace_page(request):
    return render(request,'aerospace_page.html')

def apply(request):
    return render(request,'apply.html')

def notifications(request):
    return render(request,'notifications.html')

def admitcard(request):
    return render(request,'admitcard.html')
def btech(request):
    return render(request,'btech.html')

def r_login(request):
    context = {'message':'Invalid Credentials......'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = recruiterlogin.objects.filter(Q(username=username),  Q(password=password))
        if data:
            return render(request,'loginsuccess.html')
        else:
            return render(request,'loginsuccess.html',context)
    return render(request, 'r_login.html')


def u_login(request):
    context = {'message':'Invalid Credentials......'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = recruiterlogin.objects.filter(Q(username=username),  Q(password=password))
        if data:
            return render(request,'loginsuccess.html')
        else:
            return render(request,'user_login.html',context)
    return render(request, 'user_login.html')
def examresults(request):
    return render(request,'examresults.html')
def save_enquiry(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone= request.POST.get('phone')
        previous_experience=request.POST.get('previous_experience')
        years_of_experience=request.POST.get('years_of_experience')
        en=ApplyForm(fullname=fullname,email=email,address=address,previous_experience=previous_experience,phone=phone,years_of_experience=years_of_experience)
        en.save()
    return render(request,'loginsuccess.html')