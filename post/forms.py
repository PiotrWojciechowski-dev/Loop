from django import forms

class PostForm(forms.Form):


    description = forms.CharField(
      widget=forms.Textarea(
        attrs={
          'class': 'form-control form-control-lg',
          'placeholder': 'Enter Description',
          'rows': 3
        }
      )
    )
    
        

    
