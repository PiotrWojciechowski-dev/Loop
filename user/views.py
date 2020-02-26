from django.shortcuts import render, redirect
from .forms import SignUpForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
<<<<<<< HEAD
from django.views.generic import CreateView
from django.urls import reverse_lazy
=======
from django.views.generic import CreateView, View
from django.urls import reverse_lazy, reverse
>>>>>>> master
from django.contrib.auth import get_user_model
# from .email import email

# Create your views here.

CustomUser = get_user_model()

class SignUpView(CreateView):
    model = CustomUser
    form_class = SignUpForm
<<<<<<< HEAD
    success_url = reverse_lazy('home')
=======
    success_url = reverse_lazy('signin')
>>>>>>> master
    template_name = 'signup.html'

class SignInView(View):
    template_name = 'signin.html'
    
    def signin_view(request):
        if request.method == 'POST':
<<<<<<< HEAD
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                #username = form.cleaned_data.get('username')
                #user_email = form.cleaned_data['email']
                signup_user = User.objects.get(username=username)
                ordinary_group = Group.objects.get(name='LoopUser')
                ordinary_group.user_set.add(signup_user)
                # Email.sendSignUpConfirmation(request, username, user_email)
                return render(request, 'home.html')
            else:
                form = SignUpForm()
            return render(request, 'signup.html', {'form' :form})


class SignInView(CreateView):
    model = CustomUser
    
    def signin_view(self, request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
=======
            form = AuthenticationForm(request.POST)
>>>>>>> master
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home.html')
                else:
                    return redirect('signup')
        else:
            form = AuthenticationForm()
        return render(request, 'signin.html', {'form':form})

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, self.template_name,)


class SignOutView(View):
    def logout_view(request):
        logout(request)
        return redirect(reverse('signin'))
