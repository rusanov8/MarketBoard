from enum import Enum

from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices, Enum):
    """
       Enumeration class defining user roles.
    """

    USER = 'user', _('User')
    ADMIN = 'admin', _('Admin')


class User(AbstractBaseUser):
    """
        Custom User model inheriting from AbstractBaseUser.
    """

    objects = UserManager()

    @property
    def is_admin(self):
        """
            Check if the user has admin role.
        """
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        """
            Check if the user has user role.
        """
        return self.role == UserRoles.USER

    username = None

    first_name = models.CharField(max_length=100, verbose_name=_('First name'))
    last_name = models.CharField(max_length=100, verbose_name=_('Last name'))
    email = models.EmailField(verbose_name=_('Email'), unique=True)
    phone = PhoneNumberField(verbose_name=_('Phone number'), unique=True)
    role = models.CharField(max_length=10, choices=UserRoles.choices,
                            default=UserRoles.USER, verbose_name=_('Role'))
    image = models.ImageField(upload_to='avatars/', verbose_name=_('Avatar'), blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_('User activity'), default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'users'

    @property
    def is_superuser(self):
        """
            Check if the user is a superuser.
        """

        return self.is_admin

    @property
    def is_staff(self):
        """
            Check if the user is a staff member.
        """
        return self.is_admin

    def has_perm(self, perm, obj=None):
        """
            Check if the user has a specific permission.
        """

        return self.is_admin

    def has_module_perms(self, app_label):
        """
            Check if the user has permissions to view the app.
        """

        return self.is_admin


