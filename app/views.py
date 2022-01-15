from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import signupform
from django.contrib.auth import authenticate,login,logout
from .forms import login_form
# Create your views here.
def home (request):
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
         bn = signupform(request.POST)
         print(bn)
         if bn.is_valid():
            u1 = bn.save(commit=False)
            u1.set_password(request.POST['password'])
            u1.save()
    else:
         bn = signupform()
    return render(request,'signup.html',{"bn":bn})


def log_in(request):
    if request.method == "POST":
        asd = login_form(request.POST)
        if asd.is_valid():
            username = asd.cleaned_data["email"]
            password = asd.cleaned_data["password"]
            
            print(username)
            print(password)
            us = authenticate(username=username,password=password)
            print(us)
            if us is not None:      
                     login(request,us)
                     return render(request,'profile.html')
            else:
                return HttpResponse('Invalid login')  
        else:
            return HttpResponse('is not valid')                    
    else:
        asd = login_form()   
    return render(request,"loginform.html",{"asd":asd})         
                 
                 
def profile(request):
    name = request.user
    return render (request,"profile.html",{"name":name})    


def logout(request):
     logout(request)
     return HttpResponseRedirect('/')               
                
            
            
        
        


   