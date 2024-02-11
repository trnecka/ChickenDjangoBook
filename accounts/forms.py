from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import User


class RegistrationForm(UserCreationForm):
    """
    Registration form for ChickenBook
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)

class CustomAuthenticationForm(AuthenticationForm):
    """
    Login form for ChickenBook
    """
    class Meta:
        model = User
        fields = ('email', 'password')
        