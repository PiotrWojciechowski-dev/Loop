from django.db import models
from djagno.contrib.auth import get_user_model
from datetime import datetime
from django.urls import reverse

User = get_user_model()

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

STATUS_CHOICES = [
    ('Married', 'Married'),
    ('Single', 'Single')
]

class ProfileManager(models.Manager):
    def get_auth_profile(self, profile, user, *args, **kwargs):
        try:
            obj = self.get(user=user)
            if obj:
                return obj
            except Profile.DoesNotExist:
                return None


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        default=1,
        on_delete=models.CASCADE
    )
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = User.objects.age
    gender = models.CharField(
        max_length=5,
        default=1,
        choices=GENDER_CHOICES
    )
    status = models.CharField(
        max_length=10,
        default=1,
        choices=STATUS_CHOICES
    )
    location = models.CharField(max_length=100, default='Ireland')
    bio = models.TextField(blank=True, default='I have no bio yet :(')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ProfileManager()

    def __str__(self, *args, **kwargs):
        return self.name

    def get_absolute_url(self, *args, **kwargs):
        return reverse('profiles:profiles-detail', kwargs={'id':self.pk})

    def get_create_url(self, *args, **kwargs):
        return reverse('profiles:profiles-create')
  
    def get_update_url(self, *args, **kwargs):
        return reverse('profiles:profiles-update', kwargs={'id':self.pk})

    def get_delete_url(self, *args, **kwargs):
        return reverse('profiles:profiles-delete', kwargs={'id':self.pk})

  
  
   