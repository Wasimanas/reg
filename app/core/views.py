from django.shortcuts import render, redirect 
from core.forms import CustomUserRegistration  , LoginForm
from django.urls import reverse  
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


# Create your views here.  


def custom_login(request):
    if request.method=='POST':
        form = LoginForm(request.POST) 
        if form.is_valid(): 
            print('form is valid')
            form = form.cleaned_data
            username=form.get('username')
            password=form.get('password')
            user=authenticate(username=username,password=password)  
            
            if user is not None: 
                print('user authenticated')
                login(request,user)
                messages.success(request,"Logged In") 
                return redirect(reverse('core:dashboard'))  
        return HttpResponse("Invalid credentials")
    else:
        form = LoginForm()
        return render(request,'core/login.html',{'form':form})


def login_select(request):
    return render(request,'core/login_select.html',{}) 

def registration(request): 
    if request.method=='POST': 
        form =CustomUserRegistration(request.POST,request.FILES)  
        if form.is_valid(): 
            print("working")    
            form.save()
            return redirect(reverse('core:registration_success_page'))

        else: 
            print(form.errors)
            print("not valid")   
            return redirect(reverse('core:registration'))

    else:
        form = CustomUserRegistration() 
        return render(request,'core/registration.html',{'form':form})
@login_required(login_url='/login')
def dashboard(request):   
    username = request.user.username 
    return render(request,'core/dashboard.html',{})  



def registration_success_page(request):
    return render(request,'core/success.html',{}) 


