import random
import time

from django.contrib.auth.backends import BaseBackend

from .models import CustomUser as User


class CustomBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['email']
        password = kwargs['password']

        try:
            user = User.objects.get(email=email)
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
