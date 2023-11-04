from django.contrib import admin
from .models import Userregistration,adminlogin,recruiterlogin,ApplyForm
# Register your models here.

admin.site.register(Userregistration)
admin.site.register(adminlogin)
admin.site.register(recruiterlogin)
admin.site.register(ApplyForm)