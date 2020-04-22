from django import forms
from .models import GroupChat, GroupMessage
from user.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from profiles.models import Mates


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
    
    members = forms.ModelMultipleChoiceField(label='Member', queryset=None, widget=forms.CheckboxSelectMultiple)

    def __init__(self, mates=None,*args, **kwargs):
        super(GroupChatForm, self).__init__(*args, **kwargs)
        self.fields['members'].queryset = CustomUser.objects.filter(username__in=mates)
    class Meta:
        model = GroupChat
        fields = ('name', 'groupchatImage', 'members')


    
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
                'multiple': True,
                'class': 'd-inline mt-3',
            }
        )
    )
    class Meta:
        model = GroupMessage
        fields = ('text', 'image')