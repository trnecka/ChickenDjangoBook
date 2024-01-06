from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import RegistrationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView

class RegistrationFormView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully! Now you can log in :)')
        return response
    
class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('user_profile')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Login successful!')
        return response
    
