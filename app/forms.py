from django import forms
from django.db import models
from django.forms import widgets
#from django.db.models import fields
#from .models import use
from django.contrib.auth.models import User


class signupform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {'password':forms.PasswordInput}


class login_form(forms.Form):
    #username = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget = forms.PasswordInput)

    