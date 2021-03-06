

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import View

from post.models import Post
from .models import Like



# POST LIKE VIEW
class PostLikeView(View):
  lookup = 'id'

  def get_object(self, *args, **kwargs):
    return get_object_or_404(Post, pk=self.kwargs.get(self.lookup))

  def get(self, request, state=None, id=None, *args, **kwargs):
    is_liked = Like.objects.find_is_liked(
      self.get_object(),
      request.user,
      state,
    )
    if is_liked.exists():
      is_liked.delete()
      return redirect(reverse('home'))
    else:
      Like.objects.create_like(self.get_object(), request.user, state)
      return redirect(reverse('home'))
