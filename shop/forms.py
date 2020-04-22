from django import forms

from .models import Product, Category
CATEGORY_CHOICES = [
    ('Bag', 'Bag'),
    ('Clothes', 'Clothes'),
    ('Flip Flops', 'Flip Flops'),
    ('Hats', 'Hats'),
    ('Phone Covers', 'Phone Covers'),
    ('Socks', 'Socks'),
]

class ProductForm(forms.ModelForm):
    # category = forms.ModelChoiceField(queryset = Category)
    name = forms.CharField(widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Product Name'
            }
        ))
    image = forms.ImageField(required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
        ))
    description = forms.CharField(widget=forms.Textarea(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Description',
                'rows': 4
            }
        ))
    price = forms.DecimalField(widget=forms.NumberInput(
            attrs={
                'class': 'form-control form-control-lg',
            }
    )
    )
    available = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-control form-control-lg',
        }
    )

    )
    class Meta:
        model = Product
        fields = ('category','name', 'image', 'description', 'price', 'available',)