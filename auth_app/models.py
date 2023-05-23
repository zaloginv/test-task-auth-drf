from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):

        if username is None:
            raise TypeError('Users must have a username.')

        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        user = self.create_user(username=username, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "username"
    objects = UserManager()