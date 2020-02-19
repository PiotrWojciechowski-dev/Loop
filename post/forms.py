from django import forms

class PostForm(forms.Form):
    your_post = forms.CharField(label='your post')

