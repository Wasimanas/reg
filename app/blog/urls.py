from django.urls import path 
app_name='blog'

from blog import views 


urlpatterns = [   
        path('blog-list/',views.blog_list,name='blog-list'),

        ]
