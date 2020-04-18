from django import forms
from .models import GroupChat, GroupMessage

class GroupChatForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Send a message...'
        }
    ))
    groupchatImage = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )
    
    class Meta:
        model = GroupChat
        fields = ('name', 'groupchatImage')

class GroupMessageForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(
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
        model = GroupMessage
        fields = ('text', 'image')