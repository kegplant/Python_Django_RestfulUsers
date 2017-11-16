from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class Dojos(models.Model):
#     name=models.CharField(max_length=255)
#     city=models.CharField(max_length=255)
#     state=models.CharField(max_length=2)
#     desc=models.TextField()
# class Books(models.Model):
#     name=models.CharField(max_length=255)
#     desc=models.TextField(max_length=1000,default='')
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)
class Users(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
#     books=models.ManyToManyField(Books,related_name='authors')
#     notes=models.TextField(default='')