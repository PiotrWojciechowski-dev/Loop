from django import forms

from .models import Profile
from django_countries.fields import CountryField
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ('Rather Not Say', 'Rather Not Say')
]

STATUS_CHOICES = [
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Its Complicated', 'Its Complicated'),
    ('Engaged', 'Engaged'),
    ('Dating', 'Dating'),
    ('In a relationship', 'In a relationship')

]
PRIVACY_CHOICES = [
    ('Open','Open'),
    ('Restricted', 'Restricted'),
    ('Strict', 'Strict')
]

class PrivacyForm(forms.ModelForm):
    privacy_setting = forms.ChoiceField(choices=PRIVACY_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ('privacy_setting',)

class ProfileImageForm(forms.ModelForm):
    profile_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    class Meta:
        model = Profile
        fields = ('profile_image',)

class ProfileForm(forms.ModelForm):
    fname = forms.CharField(
        label="First Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter First Name'
            }
        )
    )
    lname = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Last Name'
            }
        )
    )

    gender = forms.ChoiceField(
        required=False,
        choices=GENDER_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    status = forms.ChoiceField(
        required=False,
        choices=STATUS_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    location = CountryField().formfield(
        required=False,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    bio = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Bio',
                'rows': 4
            }
        )
    )

    profile_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    workplace = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Workplace',
                'rows': 1,
                'style':'resize:none;',
            }
        )
    )

    education = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Education',
                'rows': 1,
                'style':'resize:none;',
            }
        )
    )

    privacy_setting = forms.ChoiceField(
        required = True,
        choices=PRIVACY_CHOICES,
        widget=forms.RadioSelect)

    class Meta:
        model = Profile
        fields = ('privacy_setting', 'fname','lname', 'gender', 'status', 'location', 'bio', 'profile_image', 'workplace', 'education')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.initial['privacy_setting'] = 'Open'

    
