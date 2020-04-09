from django import forms
from .models import Post, Comment
class PostForm(forms.ModelForm):
  post = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows':'5', 'cols':'10', 'wrap':'hard',
            'class': 'post-form  form-control pt-3',
            'placeholder': 'Write a post...',
            'style':'resize:none;',
        }
    ))
  class Meta:
    model = Post
    fields = ('post',)
'''
  post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post...',
            'style': 'resize: none;'
        }
    ))
'''

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
    
