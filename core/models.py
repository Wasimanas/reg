from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.core.validators import MinLengthValidator
# Create your models here. 

USER_TYPES=( 
        ('P','Patient'),
        ('D','Doctor'),
        )



class CustomUser(AbstractUser):   
    user_type=models.CharField(max_length=1,choices=USER_TYPES) 
    profile_picture=models.ImageField(upload_to='profile_pictures/')
    address=models.TextField()
    city=models.CharField(max_length=25) 
    state=models.CharField(max_length=50) 
    pincode=models.CharField(max_length=6,validators=[MinLengthValidator(6)])    



    def __str__(self):
        return self.username 



