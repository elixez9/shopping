from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import BaseUserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phon_number = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)  #برای اینکه مشخص بشه کاربر وارد شده ادمین هست

    objects = BaseUserManager()

    def __str__(self):
        return self.email

    def USERNAME_FIELD(self):
        return self.phon_number

    def REQUIRED_FIELDS(self):
        return ['emaile']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, perm, obj=None):
        return True

    def is_staff(self):
        return self.is_admin
