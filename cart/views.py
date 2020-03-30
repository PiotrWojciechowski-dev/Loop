from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from shop.views import product_list
from .cart import Cart
from .forms import CartAddProductForm, CartClothesForm, CartHatsForm
from django.conf import settings
from profiles.models import Profile
import stripe

# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    print(request.POST)
    if request.POST.get("submit-form") == "1":
        form = CartClothesForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add2(product=product,
                    gender=cd['gender'],
                    size=cd['size'],
                    quantity=cd['quantity'],
                    update_quantity=cd['update'])
    elif request.POST.get("submit-form") == "2":
        form = CartHatsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add3(product=product,
                    colour=cd['colour'],
                    quantity=cd['quantity'],
                    update_quantity=cd['update'])
    elif request.POST.get("submit-form") == "3":
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                    quantity=cd['quantity'],
                    update_quantity=cd['update'])
    else:
        print("error")
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    if cart:
        return redirect('cart:cart_detail')
    else:
        return redirect('shop:product_list')

def cart_detail(request):
    user_profile = Profile.objects.get(user=request.user)
    cart = Cart(request) 
    current_cat = []
    for item in cart:
        item['update_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'],
                'update': True})
    return render(request, 'cart.html', {'cart': cart, 'current_cat': current_cat, 'user_profile': user_profile})
