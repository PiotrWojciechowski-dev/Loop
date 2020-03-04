from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse

from posts.models import Post
# Create your models here.

User = get_user_model()

class Like(models.Model):
  post = models.ForeignKey(
    Post,
    default=1,
    on_delete=models.CASCADE
  )
  owner = models.ForeignKey(
    User,
    default=1,
    on_delete=models.CASCADE
  )


  def __str__(self, *args, **kwargs):
    return self.post.posts