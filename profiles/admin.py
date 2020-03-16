from django.contrib import admin
from .models import Profile, Mates, Blocked

# Register your models here.
admin.site.register(Profile)
admin.site.register(Mates)
admin.site.register(Blocked)