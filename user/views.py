from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignUpForm, SignInForm, ChangePassword
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView, View, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import CustomUser
from profiles.models import Profile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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

class UserDelete(LoginRequiredMixin, DeleteView):
    template_name = 'delete_user.html'
    model = CustomUser
    success_url = reverse_lazy('signin')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['profiles'] = Profile.objects.get(user=self.request.user)
        return context


    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return redirect_to_login(request.get_full_path())
        return super(UserDelete, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(reverse('signin'))

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('home'))
        else:
            return redirect(reverse('change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'change_password.html', {'form': form})