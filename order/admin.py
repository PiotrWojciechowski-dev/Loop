from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'first_name', 'last_name', 'emailAddress', 'addressline1', 'country', 'paid']

    fieldsets = (
        ('Auth Info', {'fields': ('first_name', 'last_name', 'emailAddress', 'addressline1', 'addressline2', 'code', 'city', 'county', 'country')}),
    )

    search_fields = ['emailAddress']
    filter_horizontal = ()

    class Meta:
        model = Order

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']

    fieldsets = (
        ('Auth Info', {'fields': ('order', 'product', 'quantity', 'price')}),
    )

    search_fields = ['emailAddress']
    filter_horizontal = ()

    class Meta:
        model = OrderItem

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
