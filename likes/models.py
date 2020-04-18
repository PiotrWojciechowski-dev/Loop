from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse
from user.models import CustomUser


from post.models import Post
# Create your models here.

User = get_user_model()

class LikeManager(models.Manager):
  def find_is_liked(self, post, user, state):
    return self.filter(post=post, user=user)

  def create_like(self, post, user, state):
    like = self.create(post=post, user=user, state=True)
    like.save()

class Like(models.Model):
  post = models.ForeignKey(
    Post,
    default=1,
    on_delete=models.CASCADE
  )

  user = models.ForeignKey(
    CustomUser,
    default=1,
    on_delete=models.CASCADE
  )

  state = models.BooleanField(null=True)

  objects = LikeManager()

  def __str__(self, *args, **kwargs):
    return self.post.post
