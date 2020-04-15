from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View, DetailView, DeleteView, UpdateView, CreateView
from django.http import HttpResponseRedirect
from .models import Post, Comment, PostFile
from profiles.models import Profile, Mates
from likes.models import Like
from .forms import PostForm, CommentForm, FileForm
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

User = get_user_model()

class HomeView(LoginRequiredMixin, View):
  template_name = 'home.html'
  redirect_field_name = 'next'

  def get(self, request, *args, **kwargs):
    username = request.user.username
    if Profile.objects.filter(username=username).exists():
      post_form = PostForm()
      comment_form = CommentForm()
      file_form = FileForm()
      user_profile = Profile.objects.get(user=request.user)
      profiles = Profile.objects.all()
      users = get_user_model().objects.exclude(id=request.user.id)
      confirmed_mates = []
      try:
        mate = Mates.objects.get(current_user=request.user)
        mates = mate.users.all()
      except ObjectDoesNotExist:
        mates = None
        posts = Post.objects.filter(Q(user=request.user)).order_by('-created')
        files = PostFile.objects.filter(Q(user=request.user))
        comments = Comment.objects.filter(Q(user=request.user)).order_by('-created')
      if mates != None:
        for m in mates:
          try:
            confirmed_mate = Mates.objects.get(current_user=m, users=request.user)
            confirmed_mates.append(confirmed_mate.current_user)
          except ObjectDoesNotExist: 
            confirmed_mate = None
        posts = Post.objects.filter(Q(user__in=confirmed_mates) | Q(user=request.user)).order_by('-created')
        comments = Comment.objects.filter(Q(user__in=confirmed_mates) | Q(user=request.user)).order_by('-created')
        files = PostFile.objects.filter(Q(user__in=confirmed_mates) | Q(user=request.user))
      context = {
              'post_form': post_form, 'comment_form' : comment_form,
              'posts': posts, 'users': users, 
              'user_profile': user_profile, 'mates': mates, 
              'confirmed_mates': confirmed_mates, 'comments': comments,
              'file_form': file_form, 'files':files,
              'profiles': profiles
          }
      return render(request, self.template_name, context)
    else:
      return redirect(reverse('profiles:create_profile'))

  def post(self, request, *args, **kwargs):
    user = request.user
    if request.POST.get("submit-form") == "1":
      post_form = PostForm(request.POST)
      file_form = FileForm(request.POST, request.FILES)
      files = request.FILES.getlist('files')
      if post_form.is_valid():
        post = post_form.save(commit=False)
        post.user = user
        post.save()
        if file_form.is_valid():
          file = file_form.save(commit=False)
          print(files)
          for f in files:
            c_type = f.content_type.split("/")
            file_instance = PostFile.objects.create(files=f, post=post, user=user, content_type=c_type[0])
            file_instance.save()
    if request.POST.get("submit-form") == "2":
      comment_form = CommentForm(request.POST) 
      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        post_id = request.POST.get("id_value", "")
        comment.post_id = post_id
        comment.user = user
        text = comment_form.cleaned_data['comment']
        comment.save()
        comment_form = CommentForm()
    return redirect('home')
    args = {'post_form': post_form, 'comment_form': comment_form, 'text': text, 'file_form':file_form}
    return render(request, self.template_name, args)

  def get_object(self, *args, **kwargs):
    return get_object_or_404(
      Post,
      pk=self.kwargs.get('id')
    )

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
  fields = ['post']
  success_url = reverse_lazy('home')

class OwnerCommentMixin(OwnerMixin, LoginRequiredMixin):
  model = Comment
  fields = ['comment']
  success_url = reverse_lazy('home')


class OwnerPostEditMxin(OwnerPostMixin, OwnerEditMixin):
  fields = ['post']
  success_url = reverse_lazy('home')
  template_name = 'post/edit_post.html'

class OwnerCommentEditMxin(OwnerCommentMixin, OwnerEditMixin):
  fields = ['comment']
  success_url = reverse_lazy('home')
  template_name = 'post/edit_comment.html'

class PostUpdateView(PermissionRequiredMixin, OwnerPostEditMxin, UpdateView):
  permission_required = 'post.change_post'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)    
    context['profiles'] = Profile.objects.get(user=self.request.user)
    return context
  

class CommentUpdateView(PermissionRequiredMixin, OwnerCommentEditMxin, UpdateView):
  permission_required = 'post.change_comment'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)    
    context['profiles'] = Profile.objects.get(user=self.request.user)
    return context

class PostDeleteView(PermissionRequiredMixin ,OwnerPostEditMxin, DeleteView):
  template_name = 'post/delete_post.html'
  success_url = reverse_lazy('home')
  permission_required = 'post.delete_post'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)    
    context['profiles'] = Profile.objects.get(user=self.request.user)
    return context
  

class CommentDeleteView(PermissionRequiredMixin ,OwnerCommentEditMxin, DeleteView):
  template_name = 'post/delete_comment.html'
  success_url = reverse_lazy('home')
  permission_required = 'post.delete_comment'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)    
    context['profiles'] = Profile.objects.get(user=self.request.user)
    return context


