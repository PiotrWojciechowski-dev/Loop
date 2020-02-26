from django.db import models
from django.shortcuts import get_object_or_404

# Create your models here.
class PostManager(models.Manager):
  def get_posts(self, *args, **kwargs):
    return self.all()

  def get_post(self, post_id, *args, **kwargs):
    return get_object_or_404(self, id=post_id)

  def get_user_posts(self, owner, *args, **kwargs):
    return self.filter(owner=owner)

  def get_user_post(self, post_id, user, *args, **kwargs):
    return get_object_or_404(self, pk=post_id, owner=user)



class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    description = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

def __str__(self):
    return self.author

    

    