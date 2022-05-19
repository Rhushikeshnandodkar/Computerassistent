from distutils.command.upload import upload
from email import message
from tkinter.tix import Tree
from django.db import models
from django.contrib.auth.models import User

class product(models.Model):
    prodid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True)
    author = models.CharField(max_length=300, null=True)
    pages = models.IntegerField(null=True)
    name = models.CharField(max_length=122, null=True)
    phone = models.CharField(max_length=12, null=True)
    address = models.TextField(null=True)
    
   
class contactus(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.TextField()
    latitude = models.FloatField(null=True, default=None, verbose_name="location latitude")
    longitude = models.FloatField(null=True, default=None, verbose_name="location longitude")

class ispremium(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    is_premium = models.BooleanField(default=False)