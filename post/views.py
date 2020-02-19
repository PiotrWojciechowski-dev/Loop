from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    model = Post
    template_name = 'home.html'
    