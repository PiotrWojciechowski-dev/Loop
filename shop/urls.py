from django.urls import path
from shop import views
from django.contrib import admin

app_name = 'shop'

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/admin_add_product/', views.admin_add_product, name='admin_add_product'),
    path('admin/shop/products', admin.site.urls),

]