from django.urls import path  
app_name='core'
from core import views   
from django.contrib.auth import views as auth_views

urlpatterns = [  
        path('',views.login_select,name='login_select'),   
        path('dashboard/',views.dashboard,name='dashboard'),  
        path('success/',views.registration_success_page,name='registration_success_page'),  
        path('registration/',views.registration,name='registration'),  
        path('login/',views.custom_login,name='login'), 
        path('logout/',auth_views.LogoutView.as_view(),name='logout'),

        ]        
