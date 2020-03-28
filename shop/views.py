from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, ProductDetailImages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from cart.forms import CartAddProductForm
from .filters import ProductFilter
from profiles.models import Profile

# Create your views here.

def product_list(request, category_slug=None):
    if Profile.objects.filter(username=request.user).exists():
            user_profile = Profile.objects.get(user=request.user)
    else:
        user_profile = None
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    products_filter = ProductFilter(request.GET, queryset=Product.objects.all())
    products = products_filter.qs
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product_list = products.filter(category=category)
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
    images = product.detail_images.all()
    for image in images:
        print(image.detail_image)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'products/product_detail.html',
                  {'product': product,
                  'cart_product_form': cart_product_form,
                  'user_profile': user_profile,
                  'images': images})   