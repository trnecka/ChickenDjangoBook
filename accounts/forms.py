from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',)

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')