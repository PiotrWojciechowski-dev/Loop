from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, DetailView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.urls import reverse


# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

class PostListView(View):
  model = Post
  form = PostForm
  template_name = 'postlist.html'
  context = {}

  def get(self, request, *args, **kwargs):
    qs = self.model.objects.get_posts()
    form = self.form()
    self.context['author'] = 'Posts'
    self.context['description'] = qs
    self.context['form'] = form
    return render(request, self.template_name, self.context)

  def post(self, request, *args, **kwargs):
    form = self.form(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.owner = self.request.user
      instance.save()
      messages.success(request, 'Post has been added to feed!')
      return redirect('posts:posts-list')
    messages.error(request, 'Oop! Enter valid details!')
    return reverse('posts:posts-list')


class PostDetailView(DetailView):
  queryset = Post.objects.all()
  context_object_name = 'post'
  lookup = 'id'
  
  def get_object(self, *args, **kwargs):
    return get_object_or_404(Post, pk=self.kwargs.get(self.lookup))
  
  def get_context_data(self, *args, **kwargs):
    context = super(PostDetailView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Post Detail'
    return context  