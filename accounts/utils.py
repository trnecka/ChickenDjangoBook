
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.base_user import AbstractBaseUser

class AppTokenGenerator(PasswordResetTokenGenerator):
    """
    Generate token for ChickenBook API
    """
    def _make_hash_value(self, user: AbstractBaseUser, timestamp: int) -> str:
        return (f"{user.is_active}{user.pk}{timestamp}")

account_activation_token = AppTokenGenerator()