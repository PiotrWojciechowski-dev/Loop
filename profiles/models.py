from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.urls import reverse

User = get_user_model()

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ('Rather Not Say', 'Rather Not Say')
]

STATUS_CHOICES = [
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Its Complicated', 'Its Complicated'),
    ('Engaged', 'Engaged'),
    ('Dating', 'Dating')
]

class ProfileManager(models.Manager):
    def get_auth_profile(self, profile, user, *args, **kwargs):
        return get_object_or_404(self, pk=profile, user=user)

    def check_auth_profile(self, user, *args, **kwargs):
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
    age = models.IntegerField()
    gender = models.CharField(
        max_length=14,
        default=1,
        choices=GENDER_CHOICES
    )
    status = models.CharField(
        max_length=15,
        default=1,
        choices=STATUS_CHOICES
    )
    location = models.CharField(max_length=100, default='Ireland')
    bio = models.TextField(blank=True, default='I have no bio yet :(')
    profile_image = models.ImageField(
        upload_to='media/',
        default='default.jpg',
        blank=True
    )
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

  
  
   