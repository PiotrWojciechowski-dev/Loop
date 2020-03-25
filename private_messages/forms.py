from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    message = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Send a message...'
        }
    )
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )
    class Meta:
        model = Message
        fields = ('image','message')