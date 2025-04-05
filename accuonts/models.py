from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)  #برای اینکه مشخص بشه کاربر وارد شده ادمین هست
    USERNAME_FIELD = 'email'  #اعتبار سنجی کابرها در وررد
    REQUIRED_FIELDS = ['phone_number']
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, perm, obj=None):
        return True

    def is_staff(self):
        return self.is_admin


class OtpCode(models.Model):  # is one time password
    phone_number = models.CharField(max_length=11)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField()

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'
