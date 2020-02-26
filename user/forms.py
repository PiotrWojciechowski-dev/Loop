from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import Q
from .models import CustomUser
from datetime import date


CustomUser = get_user_model()


class SignUpForm(forms.ModelForm):

    dob = forms.DateField(
      widget=forms.DateInput
      (attrs={
        'type': 'date'
        }
      )
    )

    email = forms.EmailField(
    widget=forms.EmailInput(
      attrs={
        'placeholder': 'Enter Email Id'
      }
    )
  )

    password1 = forms.CharField(
    label='Password',
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Enter Password'
      }
    )
  )

    password2 = forms.CharField(
    label='Confirm Password',
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Confirm Password'
      }
    )
  )

    def clean_username(self, *args, **kwargs):
      username = self.cleaned_data.get('username')
      qs = get_user_model().objects.filter(username__contains=username)
      if qs.exists():
        raise forms.ValidationError('Username has already been taken!')
      else:
        return username

    def clean_dob(self, *args, **kwargs):
      dob = self.cleaned_data['dob']
      today = date.today()
      if (dob.year + 13, dob.month, dob.day) > (today.year, today.month, today.day):
        raise forms.ValidationError('Must be at least 13 or older to register')
      else:
        return dob

    def clean_email(self, *args, **kwargs):
      email = self.cleaned_data.get('email')
      qs = get_user_model().objects.filter(email__contains=email)
      if qs.exists():
          raise forms.ValidationError('Email has already been registered!')
      else:
          return email

    def clean_password2(self, *args, **kwargs):
      password1 = self.cleaned_data.get('password1')
      password2 = self.cleaned_data.get('password2')
      if password1 and password2 and password1 != password2:
          raise forms.ValidationError('Passwords did not match!')
      else:
          return password2

    def save(self, commit=True):
      user = super(SignUpForm, self).save(commit=False)
      user.set_password(self.cleaned_data['password1'])
      if commit:
          user.save()
          user.groups.add(Group.objects.get(name='LoopUser'))
      return user

    class Meta:
      model = CustomUser
      fields = ('username', 'dob', 'email')

  #first_name = forms.CharField(max_length=100, required=True)
  #last_name = forms.CharField(max_length=100, required=True)
  #email = forms.EmailField(max_length=254, help_text='eg. youremail@anyemail.com')

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
      model = CustomUser
      fields = ()
