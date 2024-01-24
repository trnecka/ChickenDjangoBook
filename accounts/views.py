from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import RegistrationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

class RegistrationFormView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully! Now you can log in :)')
        self.send_registration_email(form.cleaned_data['first_name'],
                                    form.cleaned_data['last_name'],
                                    form.cleaned_data['email'])
        return response
    
    def send_registration_email(self, first_name: str, last_name: str, to_email: str):
        """
        Method sends email
        
        Args:
            first_name (str): First name
            last_name (str): Last name
            to_email (str): Sender email

        Returns:
            int: Number of the send email
        """
        email_message = EmailMultiAlternatives(
            subject="Chicken Book Registration",
            body=get_template('accounts/templates/email/registration_email.txt').render(
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    }),
            from_email=settings.EMAIL_HOST_USER,
            to=[to_email]
            )
        email_message.attach_alternative(get_template('accounts/templates/email/registration_email.html').render(
            {
                    'first_name': first_name,
                    'last_name': last_name,
                }), "text/html")
        return email_message.send()        
    
class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm
    success_url = reverse_lazy('user_profile')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Login successful!')
        return response
    
