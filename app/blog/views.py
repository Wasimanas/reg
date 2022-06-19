from django.shortcuts import render
from blog.models import Blog
# Create your views here. 



def blog_list(request):
    blogs=Blog.objects.filter(status='published')
    return render(request,'blog/list.html',{'blogs':blogs}) 



def my_blog_list(request): 
    doctors_blogs=Blog.objects.filter(user=request.user,status='draft')
    return render(request,'blog/my_blog_list.html',{'doctors_blogs':doctors_blogs})
