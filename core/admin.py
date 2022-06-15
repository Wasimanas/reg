from django.contrib import admin
from core.models import CustomUser
from django.contrib.auth.admin import UserAdmin 
from core.forms import CustomUserRegistration
# Register your models here.   

class CustomUserAdmin(UserAdmin): 
    add_form = CustomUserRegistration  
    form = CustomUserRegistration
    model = CustomUser
    list_display = ('username','user_type')


admin.site.register(CustomUser,CustomUserAdmin)








