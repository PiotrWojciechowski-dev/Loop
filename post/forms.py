from django import forms
from .models import Post

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

    
        

    
