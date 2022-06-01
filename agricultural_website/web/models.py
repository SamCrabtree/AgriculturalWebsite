from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
     allow_empty = True
     title = models.CharField(max_length=255)
     tag = models.CharField(max_length=255)
     header_image = models.ImageField(null=True, blank=True, upload_to='Images/')
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     body = RichTextField(blank=True, null=True)
     post_date = models.DateField(auto_now_add=True)

     def __str__(self):
         return self.title + ' | ' + str(self.author)

     def get_absolute_url(self): 
         return reverse("blog_detail", args=(str(self.id)) )
    
