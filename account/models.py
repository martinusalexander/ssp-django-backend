import random
import time

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, full_name, email, password=None) -> 'CustomUser':
        """
        Creates and saves a User with the given name, email and password.
        """
        if not full_name:
            raise ValueError('User must have a full name')
        if not email:
            raise ValueError('User must have an email address')

        # User ID = 'USR' + current timestamp since epoch + random number (between 000 and 999)
        current_ts = int(time.time())
        random_int = random.randint(0, 999)
        user_id = f'USR{current_ts}{random_int:03}'

        user = self.model(
            id=user_id,
            full_name=full_name,
            email=email,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, full_name, email, password=None) -> 'CustomUser':
        """
        Creates and saves a Superuser (we do not differentiate user and superuser for now).
        """
        return self.create_user(full_name, email, password)


class CustomUser(AbstractBaseUser):
    id = models.CharField(name='id', max_length=30, primary_key=True)
    full_name = models.CharField(name='full_name', max_length=60, db_index=True)
    email = models.EmailField(name='email', max_length=60, unique=True)
    is_active = models.BooleanField(name='is_active', default=True)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(name='updated_at', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['full_name']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.full_name
