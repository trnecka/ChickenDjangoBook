from typing import Any
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class LoginBackend(BaseBackend):
    """
    Class login backend for ChickenBook.
    """
    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        """
        Authenticate method in login backend for customize login mesages during login. 

        Args:
            request (HttpRequest)
            username (str | None, optional)
            password (str | None, optional)

        Raises:
            ValidationError: Inactive account
            ValidationError: Incorrect password

        Returns:
            AbstractBaseUser | None
        """
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password) and user.is_active:
                return user
            
            if user.check_password(password) and not user.is_active:
                raise ValidationError("Your account is not active. Check your email and click on activation link!")
            
        except User.DoesNotExist:
            raise ValidationError("Please enter a correct username and password. Note that both fields may be case-sensitive.")
        
        return None
    
    def get_user(self, user_id: int) -> AbstractBaseUser | None:
        """
        The method returns the user.

        Args:
            user_id (int): ID user in the database

        Returns:
            AbstractBaseUser | None
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
