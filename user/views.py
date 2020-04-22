from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView, View, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.mixins import UserPassesTestMixin
# from .email import email

# Create your views here.

CustomUser = get_user_model()

class SignUpView(CreateView):
    model = CustomUser
    form_class = SignUpForm
    success_url = reverse_lazy('profiles:create_profile')
    template_name = 'signup.html'

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)

class SignInView(View):
    form = SignInForm
    template_name = 'signin.html'
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):
        form = SignInForm()
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user_obj')
            login(request, user)
            return redirect(reverse('home'))
        context = {
            'form' : form
        }
        return render(request, self.template_name, context)

class SignOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('signin'))

class UserDelete(UserPassesTestMixin, DeleteView):
    model = 'CustomUser'
    template_name = 'delete_user.html'
    success_url = reverse_lazy('signin')
    raise_exception = True

    def test_func(self):
        self.object = self.get_object()
        return self.object.user == self.request.user
