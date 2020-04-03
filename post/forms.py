from django import forms
from .models import Post, Comment

#class MultipleForm(forms.ModelForm):
 # action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class PostForm(forms.ModelForm):
  post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post...'
        }
    ))

  class Meta:
    model = Post
    fields = ('post',)


class CommentForm(forms.ModelForm):
  comment = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a comment...'
        }
    ))

  class Meta:
    model = Comment
    fields = ('comment',)
    
