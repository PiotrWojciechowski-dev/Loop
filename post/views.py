from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, DetailView, DeleteView, UpdateView, CreateView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



# Create your views here.


class HomeView(View):
  model = Post
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

  def get_queryset(self):
    qs = super(HomeView, self).get_queryset()
    return qs.filter(owner=self.request.user)

class OwnerMixin(object):
  def get_queryset(self):
    qs = super(OwnerMixin, self).get_queryset()
    return qs.filter(user=self.request.user)

class OwnerEditMixin(object):
  def from_valid(self, form):
    form.instance.user = self.request.user
    return super(OwnerEditMixin, self).form_valid(form)

class OwnerPostMixin(OwnerMixin, LoginRequiredMixin):
  model = Post
  fields =['post']
  success_url = reverse_lazy('home')

class OwnerPostEditMxin(OwnerPostMixin, OwnerEditMixin):
  fields = ['post']
  success_url = reverse_lazy('home')
  template_name = 'home.html'


class PostUpdateView(PermissionRequiredMixin, OwnerPostEditMxin, UpdateView):
  permission_required = 'post.change_post'

class PostDeleteView(PermissionRequiredMixin ,OwnerPostEditMxin, DeleteView):
  template_name = 'home.html'
  success_url = reverse_lazy('home')
  permission_required = 'post.delete_post'


