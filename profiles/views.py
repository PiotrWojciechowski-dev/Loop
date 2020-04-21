from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .models import Profile, Mates, Blocked
from .forms import ProfileForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView, View, DetailView, UpdateView
from django.core.exceptions import ObjectDoesNotExist

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
    if Profile.objects.filter(username=request.user).exists():
      user_profile = Profile.objects.get(user=request.user)
    else:
      user_profile = None
    form = ProfileForm()
    profile = get_object_or_404(Profile, username=username)
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
      'blocked_users': blocked_users, 'confirmed_mate': confirmed_mate
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

def change_Mates(request, operation, username):
  mate = get_user_model().objects.get(username=username)
  if operation == 'add':
    Mates.make_mates(request.user, mate)
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
    unconfirmed_mates = []
    confirmed_mates = []
    try:
      mate = Mates.objects.get(current_user=request.user)
      mates = mate.users.all()
    except ObjectDoesNotExist:
      mates = None
    try:
      blocked_by_me= Blocked.objects.get(current_user=request.user)
      blocked_users = blocked_by_me.users.all()
    except ObjectDoesNotExist:
      blocked_users = None
          
    if mates != None:
      for m in mates:
        try:
          confirmed_mate = Mates.objects.get(current_user=m, users=request.user)
          confirmed_mates.append(confirmed_mate.current_user)
        except ObjectDoesNotExist: 
          unconfirmed_mate, created = Mates.objects.get_or_create(current_user=m)
          if not created:
            unconfirmed_mate.current_user = m
            unconfirmed_mate.save()
          unconfirmed_mates.append(unconfirmed_mate.current_user)
    mate_requests = None
    context = {
      'mates':mates, 'confirmed_mates':confirmed_mates, 'unconfirmed_mates':unconfirmed_mates, 'blocked_users':blocked_users, 'mate_requests':mate_requests
    }
    return render(request, self.template_name, context)

  def get_queryset(self):
    queryset = super(OwnerMixin, self).get_queryset()
    return queryset.filter(user=self.request.user)

