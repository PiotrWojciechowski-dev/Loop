from django.contrib import admin
from .models import GroupChat, GroupMessage

# Register your models here.
admin.site.register(GroupMessage)
admin.site.register(GroupChat)