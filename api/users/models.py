from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """Custom UserManager model."""

    def create_user(self, email, full_name, password=None):

        if not email:
            raise ValueError('Users must have an email address.')
        user = self.model(
                email=self.normalize_email(email),
                full_name=full_name,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):

        user = self.create_user(
            email=email,
            full_name=full_name,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom model for User objects."""

    email = models.EmailField(
        max_length=150,
        unique=True,
        verbose_name='email address',
    )
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
