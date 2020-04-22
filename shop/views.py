from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, ProductDetailImages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from cart.forms import CartAddProductForm, CartClothesForm, CartHatsForm
from .filters import ProductFilter
from profiles.models import Profile
from .forms import ProductForm

# Create your views here.

def product_list(request, category_slug=None):
    if Profile.objects.filter(username=request.user).exists():
            user_profile = Profile.objects.get(user=request.user)
    else:
        user_profile = None
    category = None
    categories = Category.objects.all()
    products_filter = ProductFilter(request.GET, queryset=Product.objects.all())
    products = products_filter.qs
    '''Pagination code'''
    paginator = Paginator(products, 6)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
            'category': category,
            'categories': categories,
            'products': products,
            'filter': products_filter,
            'user_profile': user_profile
        }
    return render(request, 'products/products.html', context)

def product_detail(request, id, slug):
    if Profile.objects.filter(username=request.user).exists():
            user_profile = Profile.objects.get(user=request.user)
    else:
        user_profile = None
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)    
    current_category = product.category.name
    if current_category == "Clothes":
        cart_product_form = CartClothesForm()
    elif current_category == "Hats":
        cart_product_form = CartHatsForm()
    else:
        cart_product_form = CartAddProductForm()
    images = product.detail_images.all()
    return render(request,
                  'products/product_detail.html',
                  {'product': product,
                  'cart_product_form': cart_product_form,
                  'user_profile': user_profile,
                  'current_category':current_category,
                  'images': images})   


def admin_add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
        if form.cleaned_data['image'] is not None:
            forms.image = form.cleaned_data['image']
    else:
        form = ProductForm()
    
    context = {
            'form': form,
        }

    return render(request, 'products/admin_add_product.html', context)