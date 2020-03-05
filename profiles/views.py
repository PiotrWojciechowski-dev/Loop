from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .models import Profile
from .forms import ProfileForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView, View, DetailView, UpdateView

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
      profile = form.save()
      profile.save()
    return render(request, 'profile_create.html', {'profile': profile})
  else:
    form = ProfileForm()
  return render(request, 'profile_create.html',{'form':form})

class ProfileView(View):
  template_name = 'profile.html'

  def get(self, request, username, *args, **kwargs):
    form = ProfileForm()
    profile = get_object_or_404(Profile, username=username)
    users = get_user_model().objects.exclude(id=request.user.id)
    context = {
      'form':form, 'profile': profile, 'users':users
    }
    return render(request, self.template_name, context)

  def get_queryset(self):
    queryset = super(OwnerMixin, self).get_queryset()
    return queryset.filter(user=self.request.user)

  def change_friends(request, operation, username):
    friend = User.objects.get(username=username)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home')

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
  """
  def get_username():
    username = get_user_model().username
    print(username)
    return username
  """
  
  fields = ['fname','lname', 'gender', 'status', 'location', 'bio', 'profile_image',]
  #profile = get_object_or_404(Profile, username=username)
  #username = get_username()
  #success_url = reverse_lazy('profiles:profile_detail', args=[username])
  success_url = reverse_lazy('home')
  template_name = 'profile_update.html'

class ProfileUpdateView(PermissionRequiredMixin, OwnerProfileEditMixin, UpdateView):
  permission_required = 'profile.change_profile'


