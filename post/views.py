from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponseRedirect

from .forms import PostForm

from .models import Post
# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'


def get_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/post accepted/')

    else:
        form = PostForm()

    return render(request, 'home.html', {'form': form})
    