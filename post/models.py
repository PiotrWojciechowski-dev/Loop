from django.db import models
from django.shortcuts import get_object_or_404
from user.models import CustomUser

# Create your models here.

class Post(models.Model):
    post = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.user

    

    