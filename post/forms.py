from django import forms
from .models import Post, Comment, PostFile

class PostForm(forms.ModelForm):
  post = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows':'5', 'cols':'10', 'wrap':'hard',
            'class': 'post-form  form-control pt-3',
            'placeholder': 'Write a post...',
            'style':'resize:none; box-shadow: 0px 2px 3px 0px rgba(0,0,0,0.2);',
        }
    ))
  class Meta:
    model = Post
    fields = ('post',)


class FileForm(forms.ModelForm):
  files = forms.FileField(required=False, widget=forms.FileInput(
        attrs={
          'multiple': True,
          'class': 'd-inline mt-3',
          }
    ))

  class Meta:
    model = PostFile
    fields = ['files']

class CommentForm(forms.ModelForm):
  comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows':'2', 'cols':'10', 'wrap':'hard',
            'class': 'post-form  form-control pt-3',
            'placeholder': 'Write a comment...',
            'style':'resize:none; box-shadow: 0px 2px 3px 0px rgba(0,0,0,0.2);',
        }
    ))

  class Meta:
    model = Comment
    fields = ('comment',)
    
