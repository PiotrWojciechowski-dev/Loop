from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'post-form  form-control pt-3',
            'placeholder': 'Send a message...',
            'rows':'3', 'cols':'10', 'wrap':'hard',
            'style':'resize:none; box-shadow: 0px 2px 3px 0px rgba(0,0,0,0.2);',
        }
    )
    )
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'multiple': True,
                'class': 'd-inline mt-3',
            }
        )
    )
    class Meta:
        model = Message
        fields = ('text', 'image')