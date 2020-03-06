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

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='prof'
    )
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    #age = models.IntegerField()
    dob = models.DateField(null=True, blank=True)
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
        upload_to='profiles/',
        default='default.jpg',
        blank=True
    )
    username = models.TextField(max_length=30, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.__str__()


class Mates(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_mates(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_mate(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        ) 
        friend.users.remove(new_friend)
  
   