from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUser
from .forms import SignUpForm
# Register your models here.

class UserAdmin(BaseUserAdmin):
    add_form = SignUpForm

    list_display = ['username','dob','email','superuser', 'admin', 'staff', 'active']
    list_filter = ['admin', 'staff', 'active', 'groups']

    fieldsets = (
        ('Auth Info', {'fields': ('email', 'username', 'dob', 'password',)}),
        ('Permissions', {'fields': ('superuser', 'admin', 'staff', 'active', 'groups')})
    )

    search_fields = ['email']
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(CustomUser, UserAdmin)

admin.site.site_header = 'Loop Social Network Administration'
admin.site.site_title = 'Welcome To The Loop Administrative Site'
admin.site.index_title = 'Welcome To The Loop Administrative Site'