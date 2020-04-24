from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group
# Create your models here.#


class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email must be provided!!!')
        if not password:
            raise ValueError('Password can not be empty!!!')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.model(
            username=username,
            password=password,
        )
        user.set_password(password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
        


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, null=True)
    superuser = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    password = models.CharField(max_length=90, null=True, blank=True)
    username = models.CharField(max_length=30, unique=True, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self, *args, **kwargs):
	    return self.username

    def has_perm(self, perm, obj=None, *args, **kwargs):
	    return True
	
    def has_module_perms(self, app_label, *args, **kwargs):
        return True

    @property
    def is_admin(self, *args, **kwargs):
        return self.admin

    @property
    def is_staff(self, *args, **kwargs):
	    return self.staff

    @property
    def is_active(self, *args, **kwargs):
	    return self.active

    @property
    def is_superuser(self, *args, **kwargs):
        return self.superuser

    