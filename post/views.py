from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, DetailView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your views here.


class HomeView(View):
  template_name = 'home.html'

  def get(self, request, *args, **kwargs):
    form = PostForm()
    posts = Post.objects.all().order_by('-created')
    users = get_user_model().objects.exclude(id=request.user.id)
    context = {
            'form': form, 'posts': posts, 'users': users
        }
    return render(request, self.template_name, context)

  def post(self, request, *args, **kwargs):
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = request.user
      post.save()
      text = form.cleaned_data['post']
      form = PostForm()
      return redirect('home')

    args = {'form': form, 'text': text}
    return render(request, self.template_name, args)
