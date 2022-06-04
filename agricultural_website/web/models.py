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
    
class Products(models.Model):
     product_name = models.CharField(max_length=255)
     product_order = models.PositiveIntegerField()
     product_cost = models.CharField(max_length=255)
     product_image = models.ImageField(null=True, blank=True, upload_to='Images/')
     product_details = models.CharField(max_length=255)
     product_available = models.BooleanField(default=True)

     def __str__(self):
          return self.product_name + ' | $' + self.product_cost + ' | Available:' + str(self.product_available)

     def get_absolute_url(self):
          return reverse("products")





     