from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    """
    Custom manager for the User model.
    """

    def create_user(self, email, first_name, last_name, phone, image, password=None, role="user"):
        """
            Create and return a regular user with an email and password.
        """

        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            image=image,
            phone=phone,

            role=role
        )
        user.is_active = True
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None, **kwargs):
        """
            Create and return a superuser with an email, password, and admin role.
        """

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=kwargs.get('role')
        )

        return user


