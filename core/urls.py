from django.urls import path  
app_name='core'
from core import views  

urlpatterns = [  
        path('',views.login_select,name='login_select'),   
        path('dashboard/',views.dashboard,name='dashboard'),  
        path('success/',views.registration_success_page,name='registration_success_page'),
        path('patient-login/',views.patient_login,name='student_login'),
        path('doctor-login/',views.doctor_login,name='doctor_login'), 
        path('patient-registration/',views.patient_registration,name='patient_registration'),
        path('doctor-registration/',views.doctor_registration,name='doctor_registration'),

        ]
