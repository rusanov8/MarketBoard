from enum import Enum

from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices, Enum):
    USER = 'user', _('User')
    ADMIN = 'admin', _('Admin')


class User(AbstractBaseUser):

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    username = None

    first_name = models.CharField(max_length=100, verbose_name=_('First name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last name'))
    email = models.EmailField(verbose_name=_('Email'), unique=True)
    phone = PhoneNumberField(max_length=30, verbose_name=_('Phone number'), unique=True)
    role = models.CharField(max_length=10, choices=UserRoles.choices,
                            default=UserRoles.USER, verbose_name=_('Role'))
    avatar = models.ImageField(upload_to='avatars/', verbose_name=_('Avatar'), blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'users'

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


