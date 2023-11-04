from django import forms
from .models import Userregistration,recruiterlogin,userlogin

class UserRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Userregistration
        field = "all"
        exclude = ["id"]

class RecRegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = recruiterlogin
        field = "all"
        exclude = ["id"]

class UserRecForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = userlogin
        field = "all"
        exclude = ["id"]