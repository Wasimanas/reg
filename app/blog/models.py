from django.db import models
from django.conf import settings 
# Create your models here. 

BLOG_CATEGORY_CHOICES=( 
        ('M','Mental Health'),
        ('H','Heart Disease'),
        ('C','Covid19'),
        ('I','Immunization'),
        ) 


BLOG_STATUS=(
        ('draft','draft'),
        ('published','published'),
        )
class Blog(models.Model):
    category=models.CharField(max_length=1,choices=BLOG_CATEGORY_CHOICES) 
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='blogs/')
    summary=models.TextField()
    content=models.TextField() 
    status=models.CharField(max_length=9,choices=BLOG_STATUS,default='draft')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)  
    slug=models.SlugField(unique=True)


    def __str__(self):
        return f"User : {self.user.username} , Title : {self.title}" 


