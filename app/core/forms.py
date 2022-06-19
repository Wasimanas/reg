from core.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 


#('first_name','last_name','username','profile_picture','email','password1','password2','address','state','pincode','city') 

class CustomUserRegistration(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','username','profile_picture','email','password1','password2','address','state','pincode','city','user_type',) 


class LoginForm(forms.Form): 
    username=forms.CharField(max_length=150)
    password=forms.CharField(widget=forms.PasswordInput)
    
