from django import forms

from .models import Profile

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
    ('Dating', 'Dating')

]

class ProfileForm(forms.ModelForm):
    fname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter First Name'
            }
        )
    ) 
    lname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter SurName'
            }
        )
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Age'
            }
        )
    ) 
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-lg',
            }
        )
    )

    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Country'
            }
        )
    )

    bio = forms.CharField(
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
    
    class Meta:
        model = Profile
        fields = ('fname','lname', 'age', 'gender', 'status', 'location', 'bio', 'profile_image',)

    