from django.contrib import admin
from .models import Category, Product, ProductDetailImages, Review
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductImagesInline(admin.StackedInline):
    model = ProductDetailImages

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImagesInline]


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('rating', 'user_name', 'comment', 'pub_date', 'product')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

admin.site.register(Review, ReviewAdmin)