from __future__ import unicode_literals
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from django.db import models
class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['first_name'])<1:
            errors['name']='first name should not be empty!'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='invalid email!'
        return errors






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
    objects=UserManager()
    # books=models.ManyToManyField(Books,related_name='authors')
#     notes=models.TextField(default='')
class Books(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField(max_length=1000,default='')
    user=models.ForeignKey(Users,related_name='books')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
