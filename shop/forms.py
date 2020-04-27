from django import forms
from .models import Product, Category, ProductDetailImages

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset = Category.objects.all(), widget=forms.Select)
    name = forms.CharField(widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Product Name'
            }
        ))
    slug = forms.SlugField(widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Slug Name'
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
        fields = ('category','name', 'slug', 'image', 'description', 'price', 'available',)

