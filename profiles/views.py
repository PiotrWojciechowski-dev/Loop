from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .models import Profile, Mates, Blocked
from post.models import Post, PostFile
from .forms import ProfileForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView, View, DetailView, UpdateView, DeleteView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from .emails import Email
from user.models import CustomUser

User = get_user_model()

def create_profile(request):
  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      if request.user.is_authenticated:
        username = str(request.user.username)
        profile.username = username
        dob = request.user.dob
        profile.dob = dob
      if form.cleaned_data['profile_image'] is not None:
        profile.profile_image = form.cleaned_data['profile_image']
      profile.user = request.user
      profile.privacy_settings = 'open'
      profile = form.save()
      profile.save()
    return render(request, 'profile.html', {'profile': profile})
  else:
    form = ProfileForm()
  return render(request, 'profile_create.html',{'form':form})

class ProfileView(View):
  template_name = 'profile.html'

  def get(self, request,username, *args, **kwargs):
    form = ProfileForm()
    profile = get_object_or_404(Profile, username=username)
    posts = Post.objects.all().order_by('-created')
    files = PostFile.objects.filter(Q(user=request.user))
    profiles = Profile.objects.all()
    if User.objects.filter(username=request.user).exists():
      username = request.user
      user_profile = Profile.objects.get(user=request.user)

      #users = get_user_model().objects.exclude(id=request.user.id)
    else:
      username = None
    try:
      mate = Mates.objects.get(current_user=username)
      mates = mate.users.all()
    except ObjectDoesNotExist:
      mates = None
    try:
      profile_mate = Mates.objects.get(current_user=profile.user)
      profile_mates = profile_mate.users.all()
    except ObjectDoesNotExist:
      profile_mates = None
    try:
      blocked_by_user = Blocked.objects.get(current_user=profile.user)
      blocked_users = blocked_by_user.users.all()
    except ObjectDoesNotExist:
      blocked_users = None
    try:
      blocked_by_me= Blocked.objects.get(current_user=username)
      blocked_profiles = blocked_by_me.users.all()
    except ObjectDoesNotExist:
      blocked_profiles = None
    confirmed_mate = False
    if mates:
      if profile.user in mates:
        if username in profile_mates:
          confirmed_mate = True
    context = {
      'form':form, 'profile': profile, 'user_profile': user_profile, 'mates': mates, 'profile_mates': profile_mates, 'blocked_profiles':blocked_profiles,
      'blocked_users': blocked_users, 'confirmed_mate': confirmed_mate, 'posts': posts, 'profiles': profiles
    }
    return render(request, self.template_name, context)

  def get_queryset(self):
    queryset = super(OwnerMixin, self).get_queryset()
    return queryset.filter(user=self.request.user)


class OwnerMixin(object):
  def get_queryset(self):
    queryset = super(OwnerMixin, self).get_queryset()
    return queryset.filter(user=self.request.user)

class OwnerEditMixin(object):
  def from_valid(self, form):
    form.instance.user = self.request.user
    return super(OwnerEditMixin, self).form_valid(form)
  

class OwnerProfileMixin(OwnerMixin, LoginRequiredMixin):
  model = Profile
  fields =['fname','lname', 'gender', 'status', 'location', 'bio', 'profile_image',]
  success_url = reverse_lazy('profile:create_profile')

class OwnerProfileEditMixin(OwnerProfileMixin, OwnerEditMixin):
  fields = ['fname','lname', 'gender', 'status', 'location', 'bio', 'profile_image', 'privacy_settings','workplace','education']
  success_url = reverse_lazy('home')
  template_name = 'profile_update.html'

class ProfileUpdateView(PermissionRequiredMixin, OwnerProfileEditMixin, UpdateView):
  permission_required = 'profile.change_profile'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)    
    context['profiles'] = Profile.objects.get(user=self.request.user)
    return context

def change_Mates(request, operation, username):
  mate = get_user_model().objects.get(username=username)
  try:
    mate_mates = Mates.objects.get(current_user=mate).users.all()
  except ObjectDoesNotExist:
    mate_mates = []
  if operation == 'add':
    Mates.make_mates(request.user, mate)
    if request.user in mate_mates:
      Email.friendRequestAcceppted(request, mate.email, request.user)
    else:
      Email.friendRequest(request, mate.email, request.user)
  elif operation == 'lose':
      Mates.lose_mate(request.user, mate)
      Mates.lose_mate(mate, request.user)
  return redirect('home')

def block_user(request, operation, username):
  blocked = get_user_model().objects.get(username=username)
  if operation == 'block':
    Blocked.block_user(request.user, blocked)
    operation = 'lose'
    return redirect('profiles:change_Mates', operation, blocked.username)
  elif operation == 'unblock':
    Blocked.unblock_user(request.user, blocked)
    return redirect('home')

class MatesView(View):
  template_name = 'mates.html'

  def get(self, request, username, *args, **kwargs):
    if Profile.objects.filter(username=request.user).exists():
      user_profile = Profile.objects.get(user=request.user)
    else:
      user_profile = None
    unconfirmed_mates = []
    confirmed_mates = []
    mate_requests = []
    profiles = None
    uprofiles = None
    bprofiles = None
    rprofiles = None
    try:
      mate = Mates.objects.get(current_user=request.user)
      mates = mate.users.all()
    except ObjectDoesNotExist:
      mates = None

    try:
      blocked_by_me= Blocked.objects.get(current_user=request.user)
      blocked_users = blocked_by_me.users.all()
      bprofiles = Profile.objects.filter(Q(user__in=blocked_users))
    except ObjectDoesNotExist:
      blocked_users = None
    if mates != None:
      for m in mates:
        try:
          confirmed_mate = Mates.objects.get(current_user=m, users=request.user)
          confirmed_mates.append(confirmed_mate.current_user)
          profiles = Profile.objects.filter(Q(user__in=confirmed_mates))
        except ObjectDoesNotExist: 
          unconfirmed_mate, created = Mates.objects.get_or_create(current_user=m)
          if not created:
            unconfirmed_mate.current_user = m
            unconfirmed_mate.save()
          unconfirmed_mates.append(unconfirmed_mate.current_user)
          uprofiles = Profile.objects.filter(Q(user__in=unconfirmed_mates))
        
      allUsers_withOutCurrent = CustomUser.objects.exclude(username=request.user)
      for u in allUsers_withOutCurrent:
        try:
          umates = Mates.objects.get(current_user=u)
          umates_users = umates.users.all()
          if request.user in umates_users and u not in mates:
            mate_requests.append(u)
          rprofiles = Profile.objects.filter(Q(user__in=mate_requests))
        except ObjectDoesNotExist:
          umates = None
    
    else:
      allUsers_withOutCurrent = CustomUser.objects.exclude(username=request.user)
      for u in allUsers_withOutCurrent:
        try:
          umates = Mates.objects.get(current_user=u)
          umates_users = umates.users.all()
          if request.user in umates_users:
            mate_requests.append(u)
          rprofiles = Profile.objects.filter(Q(user__in=mate_requests))
        except ObjectDoesNotExist:
          umates = None



    context = {
      'mates':mates, 'confirmed_mates':confirmed_mates,
      'unconfirmed_mates':unconfirmed_mates, 'blocked_users':blocked_users,
      'mate_requests':mate_requests, 'user_profile':user_profile, 'profiles':profiles,
      'uprofiles': uprofiles, 'bprofiles': bprofiles, 'rprofiles':rprofiles
    }
    return render(request, self.template_name, context)

  def get_queryset(self):
    queryset = super(OwnerMixin, self).get_queryset()
    return queryset.filter(user=self.request.user)

