from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields

    #first_name = forms.CharField(max_length=100, required=True)
    #last_name = forms.CharField(max_length=100, required=True)
    #email = forms.EmailField(max_length=254, help_text='eg. youremail@anyemail.com')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = UserChangeForm.Meta.fields