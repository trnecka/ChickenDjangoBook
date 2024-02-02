from typing import Any
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from accounts.forms import RegistrationForm, CustomAuthenticationForm
from django.contrib.auth.views import LogoutView, LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

### These imports are for creating activation link
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .models import User
from django.shortcuts import redirect
from .utils import account_activation_token

class RegistrationFormView(CreateView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        
        messages.success(self.request, 'Account created successfully! Open your email and click on the activation link for to activate your user profile.')
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
        uidb64 = urlsafe_base64_encode(force_bytes(to_email))
        domain = get_current_site(self.request)
        scheme = self.request.scheme 
        
        user = User(
            email=to_email,
            last_name=last_name,
            first_name=first_name,
        )
        
        link = reverse("activate", kwargs={"uidb64": uidb64, "token": account_activation_token.make_token(user)})
        activate_url = f"{scheme}://{domain}{link}"
        
        email_message = EmailMultiAlternatives(
            subject="Chicken Book Registration",
            body=get_template('accounts/templates/email/registration_email.txt').render(
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'activate_url': activate_url,
                    }),
            to=[to_email]
            )
        email_message.attach_alternative(get_template('accounts/templates/email/registration_email.html').render(
            {
                    'first_name': first_name,
                    'last_name': last_name,
                    'activate_url': activate_url,
                }), "text/html")
        return email_message.send()        
    
class ChickenBookPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    subject_template_name = 'email/password_reset_email_subject.txt'
    email_template_name = 'email/password_reset_email.html'
    success_url = reverse_lazy("password_reset_done")
    
    def form_valid(self, form: Any) -> HttpResponse:
        return super().form_valid(form)
    
class ChickenBookPasswordResetDoneView(PasswordResetDoneView):
    template_name = "password_reset_done.html"
    title = "Password change successful"

class ChickenBookPasswordResetConfirmView(PasswordResetConfirmView):
    pass
    
class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomAuthenticationForm
    authentication_form = CustomAuthenticationForm
    success_url = reverse_lazy('user_profile')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Login successful!')
        return response
    
class ChickenLogoutView(LogoutView):
    pass

class VerificationPageView(View):
    def get(self, request, uidb64, token):
        try:
            email = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(email=email)
            if user.is_active == True:
                messages.warning(request, "Account was already activated. You can log in you profile.")
                return redirect('login')
            else:
                user.is_active = True
                user.save()
                messages.success(request, "Account was activated succefully.  You can log in you profile.")
        except Exception as ex:
            pass
        return redirect('login')

