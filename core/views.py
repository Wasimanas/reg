from django.shortcuts import render, redirect 
from core.forms import CustomUserRegistration 
from django.urls import reverse  
from django.contrib.auth.decorators import login_required
# Create your views here. 

def login_select(request):
    return render(request,'core/login_select.html',{}) 


def patient_registration(request):   
    if request.method=='POST': 
        print("Recieved Data") 
        return redirect(reverse("core:registration_success_page")) 
    else: 
        form=CustomUserRegistration() 
        return render(request,'core/patient_registration.html',{'form':form}) 

def doctor_registration(request):
    pass 


def patient_login(request):
    pass 


def doctor_login(request):
    pass  
def dashboard(request):  
    return render(request,'core/dashboard.html',{}) 


def registration_success_page(request):
    return render(request,'core/success.html',{}) 


