from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from .models import Profile
from .forms import ProfileForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView, View, DetailView

User = get_user_model()

def create_profile(request):
  if request.method == 'POST':
    form = ProfileForm(request.POST)
    if form.is_valid():
      profile = form.save(commit=False)
      if request.user.is_authenticated:
        username = str(request.user.username)
        profile.username = username
        dob = request.user.dob
        profile.dob = dob
      profile.user = request.user
      profile = form.save()
      profile.save()
    return render(request, 'profile_create.html', {'profile': profile})
  else:
    form = ProfileForm()
  return render(request, 'profile_create.html',{'form':form})

#def delete_profile(request):
#def update_profile(request):

class ProfileView(View):
  template_name = 'profile.html'

  def get(self, request, *args, **kwargs):
    form = ProfileForm
    profiles = Profile.objects.all().order_by('created_at')
    users = get_user_model().objects.exclude(id=request.user.id)
    context = {
      'form': form, 'profiles': profiles, 'users':users
    }
    return render(request, self.template_name, context)

  