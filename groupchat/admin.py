
from django.contrib.admin import site, ModelAdmin
from .forms import GroupChatForm
from .models import GroupChat, GroupMessage

# Register your models here.
site.register(GroupMessage)
site.register(GroupChat)