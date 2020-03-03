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

User = get_user_model()

def create_profile(request):
  if request.method == 'POST':
    form = ProfileForm(request.POST)
    if form.is_valid():
      profile = form.save(commit=False)
      #if request.user.is_authenticated:
        #username = str(request.User.username)
        #profile.username = username
      #profile.username = str(request.user)
      order = form.save()
      order.save()
    return render(request, 'profile_create.html', {'profile': profile})
  else:
    form = ProfileForm()
  return render(request, 'profile_create.html',{'form':form})

def profile_created(request):
    return render(request, 'profile_created.html', {'profile':profile})

@login_required()
def profile_detail(request):
  return render(request, 'profile.html')
#def delete_profile(request):
#def update_profile(request):
