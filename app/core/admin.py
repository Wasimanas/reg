from django.contrib import admin
from core.models import CustomUser
from django.contrib.auth.admin import UserAdmin 
from core.forms import CustomUserRegistration
# Register your models here.   

class CustomUserAdmin(UserAdmin): 
    form = CustomUserRegistration  
    model = CustomUser
    list_display = ('username','user_type')    
    fieldsets = (
        (None, {
            'fields': ( 'first_name','last_name','username','profile_picture','email','password1','password2','address','state','pincode','city','user_type' )
        }),
    )


admin.site.register(CustomUser,CustomUserAdmin)








