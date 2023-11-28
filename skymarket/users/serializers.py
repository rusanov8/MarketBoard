from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    """
      Serializer for user registration, extending Djoser's BaseUserRegistrationSerializer.

      Includes the password field for user registration.

      Args:
          BaseUserRegistrationSerializer (class): Djoser's BaseUserRegistrationSerializer class.

      Returns:
          class: UserRegistrationSerializer class.
      """

    password = serializers.CharField(style={"input_type": "password"})

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'phone', 'image')


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Custom serializer for the User model.

    Args:
        serializers (module): The serializers module from Django REST framework.
        model (class): The User model.

    Returns:
        class: CustomUserSerializer class.
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'id', 'email', 'image')
