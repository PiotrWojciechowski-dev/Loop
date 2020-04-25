from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import Q
from .models import CustomUser
from datetime import date
from django.contrib.auth import login

CustomUser = get_user_model()


class SignUpForm(forms.ModelForm):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Enter Username'
      }
    )
  )

  dob = forms.DateField(
    widget=forms.DateInput(
      attrs={
      'class': 'form-control',
      'type': 'date'
      }
    )
  )

  email = forms.EmailField(
  widget=forms.EmailInput(
    attrs={
      'class': 'form-control',
      'placeholder': 'Enter Email'
    }
  )
)

  password1 = forms.CharField(
  label='Password',
  widget=forms.PasswordInput(
    attrs={
      'class': 'form-control',
      'placeholder': 'Enter Password'
    }
  )
)

  password2 = forms.CharField(
  label='Confirm Password',
  widget=forms.PasswordInput(
    attrs={
      'class': 'form-control',
      'placeholder': 'Confirm Password'
    }
  )
)

  def clean_username(self, *args, **kwargs):
    username = self.cleaned_data.get('username')
    qs = get_user_model().objects.filter(username=username)
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
    qs = get_user_model().objects.filter(email=email)
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
      group = Group.objects.get_or_create(name='LoopUser')
      user.groups.add(Group.objects.get(name='LoopUser'))
      user.save()
    return user

  class Meta:
    model = CustomUser
    fields = ('username', 'dob', 'email', 'password1', 'password2',)


class SignInForm(forms.Form):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Username'
      }
    )
  )

  password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Password'
      }
    )
  )

  def clean(self, *args, **kwargs):
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')
    qs = get_user_model().objects.filter(username__iexact=username)
    if not qs.exists():
      raise forms.ValidationError('User does not exist!')
    user_obj = qs.first()
    if not user_obj.check_password(password):
      raise forms.ValidationError('Invalid Credentials!')
    self.cleaned_data['user_obj'] = user_obj
    return super(SignInForm, self).clean(*args, **kwargs)

  class Meta:
    model = CustomUser
    fields = ()

class ChangePassword(forms.Form):
  old_password = forms.CharField(
    label='Old',
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Enter Old Password'
      }
    )
  )

  password1 = forms.CharField(
  label='Password',
  widget=forms.PasswordInput(
    attrs={
      'class': 'form-control',
      'placeholder': 'Enter Password'
    }
  )
)

  password2 = forms.CharField(
  label='Confirm Password',
  widget=forms.PasswordInput(
    attrs={
      'class': 'form-control',
      'placeholder': 'Confirm Password'
    }
  )
)

  
class Meta:
    model = CustomUser
    fields = ('old_password', 'password1', 'password2')


def clean_password2(self, *args, **kwargs):
  password1 = self.cleaned_data.get('password1')
  password2 = self.cleaned_data.get('password2')
  old_password = self.cleaned_data.get('old_password')
  qs = get_user_model().objects.filter(username__iexact="testuser7")
  user_obj = qs.first()
  if password1 and password2 and password1 != password2:
      raise forms.ValidationError('Passwords did not match!')
  elif not user_obj.check_password(old_password):
    raise forms.ValidationError('Invalid Credentials!')
  else:
    return password2
