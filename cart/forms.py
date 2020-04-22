from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range (1, 11)]
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
SIZE_CHOICES = (
    ('Small', 'Small'),
    ('Medium', 'Medium'),
    ('Large', 'Large'),
    ('Extra Large', 'Extra Large'),
)
COLOURS_CHOICES = (
    ('Black', 'Black'),
    ('White', 'White'),
)


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

class CartClothesForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
                                
    gender = forms.TypedChoiceField(choices=GENDER_CHOICES)

    size = forms.TypedChoiceField(choices=SIZE_CHOICES)
    
                                

class CartHatsForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

    colour = forms.TypedChoiceField(choices=COLOURS_CHOICES)

