from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

def count_users():
    return User.objects.count()

def count_groups():
    return Group.objects.count()